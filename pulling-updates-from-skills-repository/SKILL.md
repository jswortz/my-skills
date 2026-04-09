---
name: Pulling Updates from Skills Repository
description: Sync local skills repository with upstream changes from obra/superpowers-skills. Use when session start indicates new upstream skills available, or when manually updating to latest versions.
---

# Updating Skills from Upstream

## Overview

Pull and merge upstream changes from obra/superpowers-skills into your local skills repository while preserving your personal modifications.

**Announce at start:** "I'm using the Updating Skills skill to sync with upstream."

## Prerequisites

Your skills repo must have a tracking branch configured. The plugin sets this up automatically (either as a fork with `origin` remote, or with an `upstream` remote).

## Detailed Workflow

For the step-by-step update process, including handling dirty working directories, fetching remotes, merging, and resolving conflicts, see [references/update-workflow.md](references/update-workflow.md).

## Common Issues

**"Already up to date"**: Your local repo is current, no action needed

**"fatal: no upstream configured"**: Your branch isn't tracking a remote branch. Check `git remote -v` to see available remotes, then set tracking with `git branch --set-upstream-to=<remote>/<branch>`

**Detached HEAD**: You're not on a branch. Ask user if they want to create a branch or check out main.

**Fast-forward fails, diverged branches**: Your local branch has commits that aren't in the remote. Regular merge will be needed, which may cause conflicts.

## Remember

- Always stash uncommitted work before merging
- Explain conflicts clearly to user
- Test that skills work after update
- User's local commits/branches are preserved
