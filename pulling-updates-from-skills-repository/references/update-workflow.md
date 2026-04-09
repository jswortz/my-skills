# Updating Skills Workflow

## The Process

### Step 1: Check Current Status
Run:
```bash
cd ~/.config/superpowers/skills
git status
```
**If working directory is dirty:** Proceed to Step 2 (stash changes)
**If clean:** Skip to Step 3

### Step 2: Stash Uncommitted Changes (if needed)
Run:
```bash
git stash push -m "Temporary stash before upstream update"
```

### Step 3: Determine Tracking Remote and Fetch
```bash
TRACKING_REMOTE=$(git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null | cut -d'/' -f1 || echo "")
if [ -n "$TRACKING_REMOTE" ]; then
    git fetch "$TRACKING_REMOTE" 2>/dev/null || true
else
    git fetch upstream 2>/dev/null || git fetch origin 2>/dev/null || true
fi
```

### Step 4: Check What's New
```bash
git log HEAD..@{u} --oneline
```
Show user: List of new commits being pulled.

### Step 5: Merge Changes
First, try a fast-forward merge:
```bash
git merge --ff-only @{u}
```
If it fails, try a regular merge:
```bash
git merge @{u}
```

### Step 6: Handle Merge Conflicts (if any)
1. Run `git status` to see conflicted files.
2. Explain conflicts and ask user how to resolve.
3. Edit files to resolve, `git add`, and `git commit`.

### Step 7: Unstash Changes (if stashed in Step 2)
```bash
git stash pop
```
Help user resolve unstash conflicts if any.

### Step 8: Verify Everything Works
```bash
${SUPERPOWERS_SKILLS_ROOT}/skills/using-skills/find-skills
```

### Step 9: Announce Completion
Tell user how many commits were merged, conflicts resolved, stashes restored, and confirm up-to-date.
