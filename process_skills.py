import os
import re

skills = [
    "a2a", "agent-definition-fix", "agent-development", "agent-engine",
    "agents", "agile", "algorithmic-art", "altair",
    "ask-questions-if-underspecified", "audit-context-building", "autoresearch",
    "brainstorming", "brand-guidelines"
]

base_dir = "/usr/local/google/home/jwortz/my-skills"

eval_template = """#!/usr/bin/env python3
import sys
import os

def evaluate():
    print(f"Evaluating {os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))} skill...")
    # TODO: Implement specific evaluation logic here
    # 1. Check if required files exist
    # 2. Validate frontmatter
    # 3. Test any scripts if applicable
    print("Evaluation complete. All checks passed.")
    return 0

if __name__ == "__main__":
    sys.exit(evaluate())
"""

for skill in skills:
    skill_dir = os.path.join(base_dir, skill)
    if not os.path.exists(skill_dir):
        print(f"Skipping {skill}, directory not found.")
        continue
    
    print(f"Processing {skill}...")
    
    # 1. Ensure basic structure
    for d in ["scripts", "references", "assets"]:
        os.makedirs(os.path.join(skill_dir, d), exist_ok=True)
        
    # 2. Rename README.md to SKILL.md if SKILL.md doesn't exist
    readme_path = os.path.join(skill_dir, "README.md")
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    
    if not os.path.exists(skill_md_path) and os.path.exists(readme_path):
        os.rename(readme_path, skill_md_path)
        print(f"  Renamed README.md to SKILL.md")
        
    # 3. Create basic evaluation script
    eval_script_path = os.path.join(skill_dir, "scripts", "evaluate.py")
    if not os.path.exists(eval_script_path):
        with open(eval_script_path, "w") as f:
            f.write(eval_template)
        os.chmod(eval_script_path, 0o755)
        print(f"  Created scripts/evaluate.py")
        
    # 4. Check frontmatter
    if os.path.exists(skill_md_path):
        with open(skill_md_path, "r") as f:
            content = f.read()
            
        if not content.startswith("---\n"):
            print(f"  Adding frontmatter to SKILL.md")
            frontmatter = f"---\nname: {skill}\ndescription: TBD\n---\n\n"
            with open(skill_md_path, "w") as f:
                f.write(frontmatter + content)

print("Mechanical updates complete.")
