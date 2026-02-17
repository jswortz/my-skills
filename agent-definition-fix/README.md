# Agent Definition Fix

## Issue Description
The Gemini CLI reported errors when loading several agent definition files in `~/.gemini/agents/`.
The errors are:
1.  `Unrecognized key(s) in object: 'color'`: The `color` property in the frontmatter is not supported.
2.  `tools: Expected array, received string`: The `tools` property is defined as a comma-separated string but must be a list.

## Objective
Fix the agent definition files by removing the unsupported `color` property and converting the `tools` property to a list format where necessary.

## Scope
All `.md` files in `~/.gemini/agents/`.

## Fix Procedure
1.  Run the provided Python script `fix_agent_definitions.py`.
    ```bash
    python3 fix_agent_definitions.py
    ```
2.  The script will iterate through all `.md` files in `~/.gemini/agents/` and modify the frontmatter.
3.  Verify the changes by checking the files.
