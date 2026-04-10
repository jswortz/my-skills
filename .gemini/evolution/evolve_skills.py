#!/usr/bin/env python3
import json
import os
import subprocess
from pathlib import Path
from typing import Any, Dict, List
# We assume the environment is set up for google-genai
# from google import genai

DEFAULT_SINK = Path.home() / ".gemini" / "skill_traces.jsonl"
SKILLS_DIR = Path.home() / "my-skills"

def get_failed_evaluations(sink_path: Path) -> List[Dict[str, Any]]:
    failed = []
    if not sink_path.exists():
        return []
    with open(sink_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                t = json.loads(line)
                if t.get("evaluated") and t.get("evaluation_result", {}).get("status") == "Fail":
                    failed.append(t)
    return failed

def evolve_skill(skill_name: str, traces: List[Dict[str, Any]]):
    skill_path = SKILLS_DIR / skill_name
    skill_md_path = skill_path / "SKILL.md"
    
    if not skill_md_path.exists():
        print(f"Skill {skill_name} not found at {skill_md_path}")
        return

    with open(skill_md_path, "r", encoding="utf-8") as f:
        current_content = f.read()

    # Construct evolution context
    context = "\n\n".join([
        f"--- Failure ---\nPrompt: {t['user_prompt']}\nFeedback: {t['evaluation_result']['feedback']}"
        for t in traces
    ])

    print(f"Evolving {skill_name} based on {len(traces)} failures...")
    
    # Use the generalist subagent to perform the evolution
    evolution_request = f"""
    Analyze the following execution failures for the skill '{skill_name}' and rewrite its 'SKILL.md' (and any relevant references) to prevent these failures.
    Follow the latest 'skill-creator' guidelines:
    - Concise is Key (keep the body lean).
    - Progressive Disclosure (move details to references/ if file grows too large).
    - Ensure valid YAML frontmatter (name and description only).

    Current content:
    {current_content}

    Failures:
    {context}
    
    The skill directory is: {skill_path}
    """
    
    # We simulate the subagent call here as this script is intended to be run
    # in an environment where 'generalist' or a similar tool is available via CLI or SDK.
    # For now, we'll keep the script as a harness that can be triggered.
    
    # Git Integration
    try:
        subprocess.run(["git", "add", "."], cwd=SKILLS_DIR, check=True)
        # Check if there are changes
        status = subprocess.run(["git", "status", "--porcelain"], cwd=SKILLS_DIR, capture_output=True, text=True).stdout
        if status:
            subprocess.run(["git", "commit", "-m", f"Auto-evolve: Improved {skill_name} based on evaluation failures"], cwd=SKILLS_DIR, check=True)
            print(f"Changes committed for {skill_name}")
        else:
            print(f"No changes generated for {skill_name}")
    except Exception as e:
        print(f"Git error: {e}")

if __name__ == "__main__":
    failed_traces = get_failed_evaluations(DEFAULT_SINK)
    if not failed_traces:
        print("No failed evaluations found. Nothing to evolve.")
    else:
        # Group by skill
        grouped = {}
        for t in failed_traces:
            s = t["skill_name"]
            grouped.setdefault(s, []).append(t)
            
        for skill_name, traces in grouped.items():
            evolve_skill(skill_name, traces)
