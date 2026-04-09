import os
import re

skills = [
    "a2a", "agent-definition-fix", "agent-development", "agent-engine",
    "agents", "agile", "algorithmic-art", "altair",
    "ask-questions-if-underspecified", "audit-context-building", "autoresearch",
    "brainstorming", "brand-guidelines"
]

base_dir = "/usr/local/google/home/jwortz/my-skills"

for skill in skills:
    skill_dir = os.path.join(base_dir, skill)
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    
    if not os.path.exists(skill_md_path):
        continue
        
    with open(skill_md_path, "r") as f:
        content = f.read()
        
    lines = content.split('\n')
    if len(lines) < 100 and skill != "agents":
        continue
        
    print(f"Applying progressive disclosure to {skill} ({len(lines)} lines)...")
    
    # Split by ## 
    sections = re.split(r'\n## ', content)
    if len(sections) <= 2:
        continue
        
    main_content = sections[0] + "\n## " + sections[1]
    details_content = "## " + "\n## ".join(sections[2:])
    
    ref_path = os.path.join(skill_dir, "references", "details.md")
    with open(ref_path, "w") as f:
        f.write(details_content)
        
    main_content += f"\n\n## Advanced Details & Examples\nFor advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).\n"
    
    with open(skill_md_path, "w") as f:
        f.write(main_content)
        
    print(f"  Moved detailed sections to references/details.md")

print("Progressive disclosure complete.")
