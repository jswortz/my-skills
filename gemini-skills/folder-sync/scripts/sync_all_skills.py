#!/usr/bin/env python3
"""
Bulk skill synchronization utility.

Automatically syncs all skills from a source skills directory (e.g., superpowers/skills/)
to a target directory (e.g., global_skills/), maintaining the same folder structure.
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import List, Set


class BulkSkillSync:
    def __init__(self, source_dir: str, target_dir: str, script_path: str):
        self.source_dir = Path(source_dir).resolve()
        self.target_dir = Path(target_dir).resolve()
        self.sync_script = Path(script_path).resolve()

        if not self.source_dir.exists():
            raise ValueError(f"Source directory does not exist: {self.source_dir}")
        if not self.target_dir.exists():
            raise ValueError(f"Target directory does not exist: {self.target_dir}")
        if not self.sync_script.exists():
            raise ValueError(f"Sync script not found: {self.sync_script}")

    def get_skills(self) -> List[Path]:
        """Get all skill directories from source."""
        skills = []
        for item in self.source_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                # Check if it looks like a skill (has SKILL.md or is a directory with files)
                if (item / 'SKILL.md').exists() or any(item.iterdir()):
                    skills.append(item)
        return sorted(skills)

    def get_existing_symlinks(self) -> Set[str]:
        """Get skill names that are already symlinks in target directory."""
        symlinks = set()
        if not self.target_dir.exists():
            return symlinks

        for item in self.target_dir.iterdir():
            if item.is_symlink():
                symlinks.add(item.name)
        return symlinks

    def sync_skill(self, skill_dir: Path, one_way: bool = True, exclude: List[str] = None) -> bool:
        """Sync a single skill directory."""
        skill_name = skill_dir.name
        target_skill_dir = self.target_dir / skill_name

        # Create target directory if it doesn't exist
        target_skill_dir.mkdir(parents=True, exist_ok=True)

        # Build sync command
        cmd = [
            sys.executable,
            str(self.sync_script),
            str(skill_dir),
            str(target_skill_dir)
        ]

        if one_way:
            cmd.append('--one-way')

        if exclude:
            cmd.append('--exclude')
            cmd.extend(exclude)

        # Run sync
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Error syncing {skill_name}: {e.stderr}", file=sys.stderr)
            return False

    def sync_all(self, one_way: bool = True, exclude: List[str] = None,
                 skip_symlinks: bool = True, dry_run: bool = False):
        """Sync all skills from source to target."""
        skills = self.get_skills()
        existing_symlinks = self.get_existing_symlinks()

        print(f"\n{'='*70}")
        print(f"Bulk Skill Sync")
        print(f"{'='*70}")
        print(f"Source: {self.source_dir}")
        print(f"Target: {self.target_dir}")
        print(f"Mode: {'One-way (source → target)' if one_way else 'Bidirectional'}")
        print(f"Skills found: {len(skills)}")
        if skip_symlinks and existing_symlinks:
            print(f"Skipping symlinks: {len(existing_symlinks)}")
        print(f"{'='*70}\n")

        if dry_run:
            print("🔍 DRY RUN - No files will be modified\n")

        synced_count = 0
        skipped_count = 0
        error_count = 0

        for skill_dir in skills:
            skill_name = skill_dir.name

            # Skip if it's already a symlink
            if skip_symlinks and skill_name in existing_symlinks:
                print(f"⏭️  Skipping {skill_name} (already a symlink)")
                skipped_count += 1
                continue

            if dry_run:
                print(f"Would sync: {skill_name}")
                synced_count += 1
                continue

            print(f"\n📁 Syncing: {skill_name}")
            print(f"   {skill_dir} → {self.target_dir / skill_name}")

            if self.sync_skill(skill_dir, one_way, exclude):
                synced_count += 1
                print(f"   ✅ Synced successfully")
            else:
                error_count += 1

        # Summary
        print(f"\n{'='*70}")
        print(f"Summary:")
        print(f"  ✅ Synced: {synced_count}")
        if skipped_count > 0:
            print(f"  ⏭️  Skipped: {skipped_count}")
        if error_count > 0:
            print(f"  ❌ Errors: {error_count}")
        print(f"{'='*70}\n")

        return error_count == 0


def main():
    parser = argparse.ArgumentParser(
        description="Bulk sync all skills from one directory to another",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Sync all skills from superpowers to global_skills (one-way)
  %(prog)s \\
    ~/.gemini/antigravity/global_skills/superpowers/skills \\
    ~/.gemini/antigravity/global_skills

  # Sync bidirectionally
  %(prog)s source/skills target --bidirectional

  # Skip skills that are already symlinks
  %(prog)s source/skills target --skip-symlinks

  # Dry run to see what would be synced
  %(prog)s source/skills target --dry-run

  # Exclude additional patterns
  %(prog)s source/skills target --exclude "*.log" "temp*"
        """
    )

    parser.add_argument('source', help='Source skills directory')
    parser.add_argument('target', help='Target directory')
    parser.add_argument('--bidirectional', action='store_true',
                       help='Bidirectional sync (default: one-way source→target)')
    parser.add_argument('--skip-symlinks', action='store_true', default=True,
                       help='Skip skills that are already symlinks in target (default: True)')
    parser.add_argument('--no-skip-symlinks', dest='skip_symlinks', action='store_false',
                       help='Do not skip symlinks')
    parser.add_argument('--exclude', nargs='+', metavar='PATTERN',
                       help='Additional patterns to exclude (e.g., "*.log" "temp*")')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be synced without actually syncing')

    args = parser.parse_args()

    # Find sync_folders.py script (should be in same directory as this script)
    script_dir = Path(__file__).parent
    sync_script = script_dir / 'sync_folders.py'

    try:
        syncer = BulkSkillSync(args.source, args.target, sync_script)
        success = syncer.sync_all(
            one_way=not args.bidirectional,
            exclude=args.exclude,
            skip_symlinks=args.skip_symlinks,
            dry_run=args.dry_run
        )

        sys.exit(0 if success else 1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
