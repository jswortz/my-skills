#!/usr/bin/env python3
import os
import re

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

for skill in batch2_skills:
    skill_dir = os.path.join(base_dir, skill)
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    if not os.path.exists(skill_md_path):
        continue
        
    with open(skill_md_path, "r") as f:
        content = f.read()

    # Clean up the previous messed up frontmatter
    # It might look like:
    # ---\nname: canvas-design\ndescription: ---
    # or similar
    
    # Let's completely remove anything that looks like the bad frontmatter
    # We will remove from the start of file until we see the first real frontmatter or content.
    while content.startswith("---\\n") or content.startswith("---\nname:"):
        # Remove literal `---\n` block if it exists
        if content.startswith("---\\n"):
            idx = content.find("---\\n\\n")
            if idx != -1:
                content = content[idx + 8:]
            else:
                idx = content.find("\\n\\n")
                if idx != -1:
                    content = content[idx + 4:]
                else:
                    content = re.sub(r'^.*?---\\n', '', content, count=1, flags=re.DOTALL)
        
        # Remove actual newlines if it was written that way
        if content.startswith("---\nname:"):
            # If the next lines are description, then another ---, keep it, it's valid!
            # Wait, if it's valid, we shouldn't remove it.
            pass
            break
            
        # Clean up any leftover literal `\n` that might be at the start
        content = content.lstrip("\\n")
        content = content.lstrip("\n")

    # Now let's check if there is a valid frontmatter
    has_frontmatter = False
    if content.startswith("---\n"):
        idx = content.find("\n---\n", 4)
        if idx != -1:
            has_frontmatter = True
            
    if not has_frontmatter:
        print(f"Adding frontmatter to {skill}")
        # Try to extract description from first paragraph
        description = "A specialized skill for " + skill.replace("-", " ")
        # Find first paragraph
        paragraphs = content.split("\n\n")
        for p in paragraphs:
            p = p.strip()
            if p and not p.startswith("#") and not p.startswith("!") and not p.startswith("[") and not p.startswith("<"):
                desc_candidate = p.replace("\n", " ").strip()
                if len(desc_candidate) > 10:
                    description = desc_candidate[:150] + ("..." if len(desc_candidate) > 150 else "")
                    break
        
        frontmatter = f"---\nname: {skill}\ndescription: {description}\n---\n\n"
        content = frontmatter + content

    # Clean up multiple --- that might exist at the start due to mess up
    if content.startswith("---\nname:"):
        # Double check if there are duplicate frontmatters
        parts = content.split("\n---\n", 2)
        if len(parts) >= 3 and parts[1].startswith("name:"):
            # Duplicate frontmatter
            content = "---\n" + parts[1] + "\n---\n" + parts[2]
            
    # Remove any literal \n that sneaked into the frontmatter
    if "---\\n" in content[:200]:
        content = content.replace("---\\n", "---\n", 1)

    # Progressive disclosure
    lines = content.split('\n')
    if len(lines) >= 100:
        print(f"Applying progressive disclosure to {skill} ({len(lines)} lines)...")
        # Split by ## 
        sections = re.split(r'\n## ', content)
        if len(sections) > 2:
            main_content = sections[0] + "\n## " + sections[1]
            details_content = "## " + "\n## ".join(sections[2:])
            
            ref_path = os.path.join(skill_dir, "references", "details.md")
            with open(ref_path, "w") as f:
                f.write(details_content)
                
            main_content += "\n\n## Advanced Details & Examples\nFor advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).\n"
            
            content = main_content
            print(f"  Moved detailed sections to references/details.md")

    with open(skill_md_path, "w") as f:
        f.write(content)

print("Fixes and progressive disclosure complete.")
