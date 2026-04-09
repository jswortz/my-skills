#!/usr/bin/env python3
import os
import re
import shutil

batch2_skills = [
    "building-secure-contracts",
    "burpsuite-project-parser",
    "canvas-design",
    "collision-zone-thinking",
    "condition-based-waiting",
    "constant-time-analysis",
    "culture-index",
    "defense-in-depth",
    "demo-enhancement-advisor",
    "demo-qa-coordinator",
    "differential-review",
    "dispatching-parallel-agents",
    "doc-coauthoring",
    "docx",
    "dssib-vertex-pipelines"
]

base_dir = "/usr/local/google/home/jwortz/my-skills"

eval_template = """#!/usr/bin/env python3
import sys
import os

def evaluate():
    skill_name = "{skill_name}"
    print(f"Evaluating {{skill_name}} skill...")
    
    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    
    # 1. Check if required files exist
    if not os.path.exists(skill_md_path):
        print("Error: SKILL.md not found.")
        return 1
        
    # 2. Validate frontmatter
    with open(skill_md_path, "r") as f:
        content = f.read()
        if not content.startswith("---\\n"):
            print("Error: SKILL.md is missing YAML frontmatter.")
            return 1
            
    print("Evaluation complete. All checks passed.")
    return 0

if __name__ == "__main__":
    sys.exit(evaluate())
"""

for skill in batch2_skills:
    skill_dir = os.path.join(base_dir, skill)
    if not os.path.exists(skill_dir):
        print(f"Skipping {skill}, directory not found.")
        continue
    
    print(f"\\n--- Processing {skill} ---")
    
    # 1. Ensure basic structure
    for d in ["scripts", "references", "assets"]:
        os.makedirs(os.path.join(skill_dir, d), exist_ok=True)
        
    # 2. Handle SKILL.md / README.md logic
    readme_path = os.path.join(skill_dir, "README.md")
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    
    if not os.path.exists(skill_md_path):
        if os.path.exists(readme_path):
            os.rename(readme_path, skill_md_path)
            print("  Renamed README.md to SKILL.md")
        else:
            # Check for nested SKILL.md
            nested_paths = [
                os.path.join(skill_dir, "skills", "SKILL.md"),
                os.path.join(skill_dir, skill, "SKILL.md")
            ]
            moved = False
            for p in nested_paths:
                if os.path.exists(p):
                    os.rename(p, skill_md_path)
                    print(f"  Moved nested SKILL.md from {p} to root")
                    moved = True
                    break
            if not moved:
                print("  Warning: No SKILL.md or README.md found to use as root.")
                continue

    # 3. Create basic evaluation script
    eval_script_path = os.path.join(skill_dir, "scripts", "evaluate.py")
    with open(eval_script_path, "w") as f:
        f.write(eval_template.format(skill_name=skill))
    os.chmod(eval_script_path, 0o755)
    print("  Created scripts/evaluate.py")
        
    # 4. Read SKILL.md
    with open(skill_md_path, "r") as f:
        content = f.read()

    # 5. Check and add frontmatter
    if not content.startswith("---\\n"):
        print("  Adding frontmatter to SKILL.md")
        
        # Try to extract description from first paragraph
        description = "A specialized skill for " + skill.replace("-", " ")
        paragraphs = content.split("\\n\\n")
        for p in paragraphs:
            if p.strip() and not p.startswith("#") and not p.startswith("!") and not p.startswith("["):
                desc_candidate = p.strip().replace("\\n", " ")
                if len(desc_candidate) > 10:
                    description = desc_candidate[:150] + ("..." if len(desc_candidate) > 150 else "")
                    break
                    
        frontmatter = f"---\\nname: {skill}\\ndescription: {description}\\n---\\n\\n"
        content = frontmatter + content
        with open(skill_md_path, "w") as f:
            f.write(content)

    # 6. Progressive disclosure
    lines = content.split('\\n')
    if len(lines) >= 100:
        print(f"  Applying progressive disclosure ({len(lines)} lines)...")
        # Split by ## 
        sections = re.split(r'\\n## ', content)
        if len(sections) > 2:
            main_content = sections[0] + "\\n## " + sections[1]
            details_content = "## " + "\\n## ".join(sections[2:])
            
            ref_path = os.path.join(skill_dir, "references", "details.md")
            with open(ref_path, "w") as f:
                f.write(details_content)
                
            main_content += f"\\n\\n## Advanced Details & Examples\\nFor advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).\\n"
            
            with open(skill_md_path, "w") as f:
                f.write(main_content)
            print("  Moved detailed sections to references/details.md")

print("\\nBatch 2 updates complete.")
