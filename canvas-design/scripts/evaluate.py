#!/usr/bin/env python3
import sys
import os

def evaluate():
    skill_name = "canvas-design"
    print(f"Evaluating {skill_name} skill...")
    
    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    
    # 1. Check if required files exist
    if not os.path.exists(skill_md_path):
        print("Error: SKILL.md not found.")
        return 1
        
    # 2. Validate frontmatter
    with open(skill_md_path, "r") as f:
        content = f.read()
        if not content.startswith("---\n"):
            print("Error: SKILL.md is missing YAML frontmatter.")
            return 1
            
    print("Evaluation complete. All checks passed.")
    return 0

if __name__ == "__main__":
    sys.exit(evaluate())
