import os
import re

AGENTS_DIR = os.path.expanduser("~/.gemini/agents")

def fix_file(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    # Extract frontmatter
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        # try without newline after first ---
        match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not match:
            print(f"Skipping {filepath}: No frontmatter found")
            return

    frontmatter_content = match.group(1)
    # The full match includes the delimiters, but we want to modify the content inside or the whole block
    # It's safer to reconstruct the block
    
    new_frontmatter_content = frontmatter_content

    # remove color
    if re.search(r'^color:.*$', new_frontmatter_content, re.MULTILINE):
        print(f"Removing color from {filepath}")
        new_frontmatter_content = re.sub(r'^color:.*\n?', '', new_frontmatter_content, flags=re.MULTILINE)

    # fix tools
    tools_match = re.search(r'^tools:\s*(.*)$', new_frontmatter_content, re.MULTILINE)
    if tools_match:
        tools_val = tools_match.group(1).strip()
        if not tools_val.startswith('['):
            # It's a string, convert to list
            raw_val = tools_val
            # Remove quotes if present
            if (raw_val.startswith('"') and raw_val.endswith('"')) or \
               (raw_val.startswith("'") and raw_val.endswith("'")):
                raw_val = raw_val[1:-1]
            
            # Split by comma
            tools_list = [t.strip() for t in raw_val.split(',') if t.strip()]
            
            # Form new list string
            new_tools_val = '[' + ', '.join([f'"{t}"' for t in tools_list]) + ']'
            
            print(f"Fixing tools in {filepath}: {tools_val} -> {new_tools_val}")
            new_frontmatter_content = re.sub(r'^tools:.*$', f'tools: {new_tools_val}', new_frontmatter_content, flags=re.MULTILINE)

    if new_frontmatter_content != frontmatter_content:
        new_content = content.replace(frontmatter_content, new_frontmatter_content)
        try:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        except Exception as e:
            print(f"Error writing {filepath}: {e}")
    else:
        print(f"No changes for {filepath}")

def main():
    if not os.path.exists(AGENTS_DIR):
        print(f"Directory {AGENTS_DIR} does not exist.")
        return

    print(f"Scanning {AGENTS_DIR}...")
    for filename in os.listdir(AGENTS_DIR):
        if filename.endswith(".md"):
            fix_file(os.path.join(AGENTS_DIR, filename))

if __name__ == "__main__":
    main()
