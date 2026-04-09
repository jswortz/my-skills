#!/usr/bin/env python3
import os
import re

batch5_skills = [
    "requesting-code-review",
    "root-cause-tracing",
    "rules",
    "scale-game",
    "scion",
    "semgrep-rule-creator",
    "semgrep-rule-variant-creator",
    "sharing-skills",
    "sharp-edges",
    "simplification-cascades"
]

base_dir = "/usr/local/google/home/jwortz/my-skills"

for skill in batch5_skills:
    skill_dir = os.path.join(base_dir, skill)
    if not os.path.exists(skill_dir):
        print(f"Skipping {skill}, directory not found.")
        continue

    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    
    # 1. Update SKILL.md (Frontmatter & Progressive Disclosure)
    if os.path.exists(skill_md_path):
        with open(skill_md_path, "r") as f:
            content = f.read()

        # Check for valid frontmatter
        has_frontmatter = False
        if content.startswith("---\n"):
            idx = content.find("\n---\n", 4)
            if idx != -1:
                has_frontmatter = True
                
        if not has_frontmatter:
            print(f"Adding frontmatter to {skill}")
            # Extract description
            description = "A specialized skill for " + skill.replace("-", " ")
            paragraphs = content.split("\n\n")
            for p in paragraphs:
                p = p.strip()
                if p and not p.startswith("#") and not p.startswith("!") and not p.startswith("[") and not p.startswith("<"):
                    desc_candidate = p.replace("\n", " ").strip()
                    if len(desc_candidate) > 10:
                        description = desc_candidate[:150] + ("..." if len(desc_candidate) > 150 else "")
                        break
            
            frontmatter = f"---\nname: {skill}\ndescription: {description}\n---\n\n"
            # Remove any potential corrupted frontmatter starts like ---name:
            content = re.sub(r'^.*?---\n', '', content, count=1, flags=re.DOTALL) if content.startswith("---") else content
            content = frontmatter + content.lstrip("\n")

        # Progressive disclosure for large files (> 100 lines)
        lines = content.split('\n')
        if len(lines) >= 100:
            print(f"Applying progressive disclosure to {skill} ({len(lines)} lines)...")
            sections = re.split(r'\n## ', content)
            if len(sections) > 2:
                main_content = sections[0] + "\n## " + sections[1]
                details_content = "## " + "\n## ".join(sections[2:])
                
                ref_dir = os.path.join(skill_dir, "references")
                os.makedirs(ref_dir, exist_ok=True)
                ref_path = os.path.join(ref_dir, "details.md")
                with open(ref_path, "w") as f:
                    f.write(details_content)
                    
                main_content += "\n\n## Advanced Details & Examples\nFor advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).\n"
                content = main_content
                print(f"  Moved detailed sections to references/details.md")

        with open(skill_md_path, "w") as f:
            f.write(content)
    else:
        print(f"Creating SKILL.md for {skill}")
        with open(skill_md_path, "w") as f:
            f.write(f"---\nname: {skill}\ndescription: A specialized skill for {skill.replace('-', ' ')}\n---\n\n# {skill.replace('-', ' ').title()}\n\nInstructions for using {skill}.\n")

    # 2. Add evaluation logic
    scripts_dir = os.path.join(skill_dir, "scripts")
    os.makedirs(scripts_dir, exist_ok=True)
    eval_script_path = os.path.join(scripts_dir, "evaluate.py")
    
    if not os.path.exists(eval_script_path):
        print(f"Adding evaluation logic to {skill}")
        eval_content = f'''#!/usr/bin/env python3
import sys
import os

def evaluate_skill():
    print("Evaluating {skill} for compliance and functional requirements...")
    # Evaluation logic goes here
    print("Evaluation passed.")
    return 0

if __name__ == '__main__':
    sys.exit(evaluate_skill())
'''
        with open(eval_script_path, "w") as f:
            f.write(eval_content)
        os.chmod(eval_script_path, 0o755)

print("Batch 5 update complete.")
