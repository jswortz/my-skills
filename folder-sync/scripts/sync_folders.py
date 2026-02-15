#!/usr/bin/env python3
"""
Bidirectional folder synchronization script.

Keeps two folders in sync by copying new/modified files between them.
Supports symlinks, exclusion patterns, and one-time or continuous sync modes.
"""

import os
import sys
import argparse
import shutil
import time
from pathlib import Path
from typing import Set, List, Optional
import fnmatch


class FolderSync:
    def __init__(self, source: str, target: str, exclude_patterns: Optional[List[str]] = None):
        self.source = Path(source).resolve()
        self.target = Path(target).resolve()
        self.exclude_patterns = exclude_patterns or [
            '.git', '__pycache__', '*.pyc', '.DS_Store',
            'node_modules', '.venv', 'venv'
        ]

        if not self.source.exists():
            raise ValueError(f"Source directory does not exist: {self.source}")
        if not self.target.exists():
            raise ValueError(f"Target directory does not exist: {self.target}")

    def should_exclude(self, path: Path) -> bool:
        """Check if a path should be excluded based on patterns."""
        # Try to get relative path from either source or target
        try:
            if path.is_relative_to(self.source):
                rel_path = str(path.relative_to(self.source))
            elif path.is_relative_to(self.target):
                rel_path = str(path.relative_to(self.target))
            else:
                rel_path = str(path)
        except (ValueError, AttributeError):
            # Fallback for older Python versions or if path is not relative
            rel_path = str(path)

        for pattern in self.exclude_patterns:
            if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(path.name, pattern):
                return True
            # Check if any parent directory matches
            for parent in path.parents:
                if fnmatch.fnmatch(parent.name, pattern):
                    return True
        return False

    def get_all_files(self, directory: Path) -> Set[Path]:
        """Get all files in a directory recursively, excluding patterns."""
        files = set()
        for item in directory.rglob('*'):
            if self.should_exclude(item):
                continue
            if item.is_file() or item.is_symlink():
                files.add(item.relative_to(directory))
        return files

    def copy_file(self, src: Path, dst: Path, dst_base: Path, reason: str = "new"):
        """Copy a file or symlink from source to destination."""
        dst.parent.mkdir(parents=True, exist_ok=True)

        if src.is_symlink():
            # Handle symlinks specially
            link_target = os.readlink(src)
            if dst.exists() or dst.is_symlink():
                dst.unlink()
            os.symlink(link_target, dst)
            print(f"  [SYMLINK] {reason}: {dst.relative_to(dst_base)}")
        else:
            shutil.copy2(src, dst)
            print(f"  [COPY] {reason}: {dst.relative_to(dst_base)}")

    def sync_direction(self, from_dir: Path, to_dir: Path, label: str):
        """Sync files from one directory to another."""
        print(f"\n{label}:")

        from_files = self.get_all_files(from_dir)
        to_files = self.get_all_files(to_dir)

        # Files that exist in source but not in target
        new_files = from_files - to_files
        # Files that exist in both but may be modified
        common_files = from_files & to_files

        copied = 0

        # Copy new files
        for rel_path in sorted(new_files):
            src = from_dir / rel_path
            dst = to_dir / rel_path
            self.copy_file(src, dst, to_dir, reason="new")
            copied += 1

        # Update modified files
        for rel_path in sorted(common_files):
            src = from_dir / rel_path
            dst = to_dir / rel_path

            # Skip if both are symlinks pointing to same target
            if src.is_symlink() and dst.is_symlink():
                if os.readlink(src) == os.readlink(dst):
                    continue

            # Compare modification times (skip symlinks for mtime comparison)
            if not src.is_symlink() and not dst.is_symlink():
                if src.stat().st_mtime <= dst.stat().st_mtime:
                    continue

            self.copy_file(src, dst, to_dir, reason="updated")
            copied += 1

        if copied == 0:
            print(f"  No changes detected")
        else:
            print(f"  Total: {copied} files synced")

    def sync_once(self, bidirectional: bool = True):
        """Perform a one-time sync."""
        print(f"\n{'='*60}")
        print(f"Syncing folders:")
        print(f"  Source: {self.source}")
        print(f"  Target: {self.target}")
        print(f"  Mode: {'Bidirectional' if bidirectional else 'One-way'}")
        print(f"{'='*60}")

        # Source -> Target
        self.sync_direction(self.source, self.target, "Source → Target")

        # Target -> Source (if bidirectional)
        if bidirectional:
            self.sync_direction(self.target, self.source, "Target → Source")

        print(f"\n{'='*60}")
        print("Sync complete!")
        print(f"{'='*60}\n")

    def watch(self, interval: int = 5, bidirectional: bool = True):
        """Watch and sync continuously."""
        print(f"Starting watch mode (checking every {interval}s, Ctrl+C to stop)...")
        try:
            while True:
                self.sync_once(bidirectional)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nWatch mode stopped.")


def main():
    parser = argparse.ArgumentParser(
        description="Bidirectional folder synchronization tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # One-time bidirectional sync
  %(prog)s /path/to/source /path/to/target

  # One-way sync (source to target only)
  %(prog)s /path/to/source /path/to/target --one-way

  # Continuous watch mode
  %(prog)s /path/to/source /path/to/target --watch

  # Watch with custom interval
  %(prog)s /path/to/source /path/to/target --watch --interval 10

  # Exclude additional patterns
  %(prog)s /path/to/source /path/to/target --exclude "*.log" "temp*"
        """
    )

    parser.add_argument('source', help='Source directory')
    parser.add_argument('target', help='Target directory')
    parser.add_argument('--watch', action='store_true',
                       help='Watch and sync continuously')
    parser.add_argument('--interval', type=int, default=5,
                       help='Watch interval in seconds (default: 5)')
    parser.add_argument('--one-way', action='store_true',
                       help='One-way sync (source to target only)')
    parser.add_argument('--exclude', nargs='+', metavar='PATTERN',
                       help='Additional patterns to exclude (e.g., "*.log" "temp*")')

    args = parser.parse_args()

    try:
        exclude_patterns = None
        if args.exclude:
            # Use default patterns + user patterns
            exclude_patterns = [
                '.git', '__pycache__', '*.pyc', '.DS_Store',
                'node_modules', '.venv', 'venv'
            ] + args.exclude

        syncer = FolderSync(args.source, args.target, exclude_patterns)

        if args.watch:
            syncer.watch(interval=args.interval, bidirectional=not args.one_way)
        else:
            syncer.sync_once(bidirectional=not args.one_way)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
