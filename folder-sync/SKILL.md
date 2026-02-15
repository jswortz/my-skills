---
name: folder-sync
description: Keep two directories synchronized by automatically copying new and modified files between them. Use this skill when you need to (1) Sync skills or code between different locations, (2) Bulk sync all skills from a source directory to target, (3) Maintain backup copies of directories, (4) Keep development and deployment folders in sync, (5) Mirror directory contents with symlink support, or (6) Set up continuous folder synchronization with watch mode.
---

# Folder Sync

Keep two directories synchronized with bidirectional or one-way file copying, including support for symlinks, exclusion patterns, and continuous watch mode.

## Quick Start

Use the `sync_folders.py` script for all synchronization tasks:

```bash
# One-time bidirectional sync
python scripts/sync_folders.py /path/to/source /path/to/target

# One-way sync (source to target only)
python scripts/sync_folders.py /path/to/source /path/to/target --one-way

# Continuous watch mode (checks every 5 seconds)
python scripts/sync_folders.py /path/to/source /path/to/target --watch

# Watch with custom interval
python scripts/sync_folders.py /path/to/source /path/to/target --watch --interval 10
```

## Common Use Cases

### Syncing Global Skills

Sync skills from a development directory to the global skills directory:

```bash
python scripts/sync_folders.py \
  ~/.gemini/antigravity/global_skills/superpowers/skills/my-skill \
  ~/.gemini/antigravity/global_skills/my-skill \
  --one-way
```

### Bidirectional Development Sync

Keep two working directories in sync during development:

```bash
python scripts/sync_folders.py \
  ~/projects/my-app \
  ~/backups/my-app \
  --watch
```

### Excluding Files

Exclude specific patterns (in addition to defaults like `.git`, `node_modules`):

```bash
python scripts/sync_folders.py /source /target \
  --exclude "*.log" "temp*" "*.tmp"
```

## Bulk Sync All Skills

The `sync_all_skills.py` script automatically syncs all skills from a source directory to a target directory.

### Sync All Skills from Superpowers

```bash
# Sync all skills from superpowers/skills to global_skills
python scripts/sync_all_skills.py \
  ~/.gemini/antigravity/global_skills/superpowers/skills \
  ~/.gemini/antigravity/global_skills
```

### Bulk Sync Options

```bash
# Dry run to preview what will be synced
python scripts/sync_all_skills.py /source/skills /target --dry-run

# Bidirectional sync (changes go both ways)
python scripts/sync_all_skills.py /source/skills /target --bidirectional

# Don't skip existing symlinks
python scripts/sync_all_skills.py /source/skills /target --no-skip-symlinks

# Exclude additional patterns
python scripts/sync_all_skills.py /source/skills /target --exclude "*.bak"
```

### Bulk Sync Script Reference

**Location:** `scripts/sync_all_skills.py`

**Parameters:**
- `source`: Source skills directory (required)
- `target`: Target directory (required)
- `--bidirectional`: Enable bidirectional sync (default: one-way)
- `--skip-symlinks`: Skip skills that are already symlinks in target (default: True)
- `--no-skip-symlinks`: Don't skip symlinks
- `--exclude PATTERN [PATTERN ...]`: Additional exclusion patterns (optional)
- `--dry-run`: Preview what would be synced without making changes (optional)

**Features:**
- Automatically discovers all skill directories in source
- Creates target directories as needed
- Skips skills that are already symlinks (configurable)
- Shows detailed progress for each skill
- Provides summary with sync count, skipped count, and errors

## Features

- **Bidirectional sync**: Changes in either directory are propagated to the other
- **One-way sync**: Use `--one-way` flag for source-to-target only
- **Symlink support**: Properly handles symbolic links
- **Smart exclusions**: Automatically excludes `.git`, `__pycache__`, `node_modules`, etc.
- **Custom exclusions**: Add your own patterns with `--exclude`
- **Watch mode**: Continuous monitoring and syncing with configurable interval
- **Modification time checking**: Only copies files that are newer

## Default Exclusions

The following patterns are excluded by default:
- `.git`
- `__pycache__`
- `*.pyc`
- `.DS_Store`
- `node_modules`
- `.venv`, `venv`

Add custom exclusions with the `--exclude` flag.

## Script Reference

**Location:** `scripts/sync_folders.py`

**Parameters:**
- `source`: Source directory path (required)
- `target`: Target directory path (required)
- `--watch`: Enable continuous sync mode (optional)
- `--interval N`: Watch interval in seconds, default 5 (optional)
- `--one-way`: One-way sync from source to target only (optional)
- `--exclude PATTERN [PATTERN ...]`: Additional exclusion patterns (optional)

**Exit codes:**
- `0`: Success
- `1`: Error (invalid directories, permission issues, etc.)
