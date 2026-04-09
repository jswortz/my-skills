---
name: gemini-in-chrome-troubleshooting
description: Diagnoses and fixes Gemini in Chrome MCP extension connectivity issues. Use when mcp__gemini-in-chrome__* tools fail or return connection errors.
---

# Gemini in Chrome MCP Troubleshooting

Use this skill when Gemini in Chrome MCP tools fail to connect or work unreliably.

## When to Use

- `mcp__gemini-in-chrome__*` tools fail with "Browser extension is not connected"
- Browser automation works erratically or times out
- After updating Gemini CLI or Gemini.app
- When switching between Gemini CLI CLI and Gemini.app (Cowork)
- Native host process is running but MCP tools still fail

## When NOT to Use

- **Linux or Windows users** - This skill covers macOS-specific paths and tools (`~/Library/Application Support/`, `osascript`)
- General Chrome automation issues unrelated to the Gemini extension
- Gemini.app desktop issues (not browser-related)
- Network connectivity problems
- Chrome extension installation issues (use Chrome Web Store support)

## The Gemini.app vs Gemini CLI Conflict (Primary Issue)

**Background:** When Gemini.app added Cowork support (browser automation from the desktop app), it introduced a competing native messaging host that conflicts with Gemini CLI CLI.

### Two Native Hosts, Two Socket Formats

| Component | Native Host Binary | Socket Location |
|-----------|-------------------|-----------------|
| **Gemini.app (Cowork)** | `/Applications/Gemini.app/Contents/Helpers/chrome-native-host` | `/tmp/gemini-mcp-browser-bridge-$USER/<PID>.sock` |
| **Gemini CLI CLI** | `~/.local/share/gemini/versions/<version> --chrome-native-host` | `$TMPDIR/gemini-mcp-browser-bridge-$USER` (single file) |

### Why They Conflict

1. Both register native messaging configs in Chrome:
   - `com.gemini.gemini_browser_extension.json` → Gemini.app helper
   - `com.gemini.gemini_code_browser_extension.json` → Gemini CLI wrapper

2. Chrome extension requests a native host by name
3. If the wrong config is active, the wrong binary runs
4. The wrong binary creates sockets in a format/location the MCP client doesn't expect
5. Result: "Browser extension is not connected" even though everything appears to be running

### The Fix: Disable Gemini.app's Native Host

**If you use Gemini CLI CLI for browser automation (not Cowork):**

```bash
# Disable the Gemini.app native messaging config
mv ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/com.gemini.gemini_browser_extension.json \
   ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/com.gemini.gemini_browser_extension.json.disabled

# Ensure the Gemini CLI config exists and points to the wrapper
cat ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/com.gemini.gemini_code_browser_extension.json
```

**If you use Cowork (Gemini.app) for browser automation:**

```bash
# Disable the Gemini CLI native messaging config
mv ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/com.gemini.gemini_code_browser_extension.json \
   ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/com.gemini.gemini_code_browser_extension.json.disabled
```

**You cannot use both simultaneously.** Pick one and disable the other.

### Toggle Script

Add this to `~/.zshrc` or run directly:

```bash
chrome-mcp-toggle() {
    local CONFIG_DIR=~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts
    local GEMINI_APP="$CONFIG_DIR/com.gemini.gemini_browser_extension.json"
    local GEMINI_CLI="$CONFIG_DIR/com.gemini.gemini_code_browser_extension.json"

    if [[ -f "$GEMINI_APP" && ! -f "$GEMINI_APP.disabled" ]]; then
        # Currently using Gemini.app, switch to Gemini CLI
        mv "$GEMINI_APP" "$GEMINI_APP.disabled"
        [[ -f "$GEMINI_CLI.disabled" ]] && mv "$GEMINI_CLI.disabled" "$GEMINI_CLI"
        echo "Switched to Gemini CLI CLI"
        echo "Restart Chrome and Gemini CLI to apply"
    elif [[ -f "$GEMINI_CLI" && ! -f "$GEMINI_CLI.disabled" ]]; then
        # Currently using Gemini CLI, switch to Gemini.app
        mv "$GEMINI_CLI" "$GEMINI_CLI.disabled"
        [[ -f "$GEMINI_APP.disabled" ]] && mv "$GEMINI_APP.disabled" "$GEMINI_APP"
        echo "Switched to Gemini.app (Cowork)"
        echo "Restart Chrome to apply"
    else
        echo "Current state unclear. Check configs:"
        ls -la "$CONFIG_DIR"/com.gemini*.json* 2>/dev/null
    fi
}
```

Usage: `chrome-mcp-toggle` then restart Chrome (and Gemini CLI if switching to CLI).

## Quick Diagnosis

```bash
# 1. Which native host binary is running?
ps aux | grep chrome-native-host | grep -v grep
# Gemini.app: /Applications/Gemini.app/Contents/Helpers/chrome-native-host
# Gemini CLI: ~/.local/share/gemini/versions/X.X.X --chrome-native-host

# 2. Where is the socket?
# For Gemini CLI (single file in TMPDIR):
ls -la "$(getconf DARWIN_USER_TEMP_DIR)/gemini-mcp-browser-bridge-$USER" 2>&1

# For Gemini.app (directory with PID files):
ls -la /tmp/gemini-mcp-browser-bridge-$USER/ 2>&1

# 3. What's the native host connected to?
lsof -U 2>&1 | grep gemini-mcp-browser-bridge

# 4. Which configs are active?
ls ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/com.gemini*.json
```

## Critical Insight

**MCP connects at startup.** If the browser bridge wasn't ready when Gemini CLI started, the connection will fail for the entire session. The fix is usually: ensure Chrome + extension are running with correct config, THEN restart Gemini CLI.

## Full Reset Procedure (Gemini CLI CLI)

```bash
# 1. Ensure correct config is active
mv ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/com.gemini.gemini_browser_extension.json \
   ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/com.gemini.gemini_browser_extension.json.disabled 2>/dev/null

# 2. Update the wrapper to use latest Gemini CLI version
cat > ~/.gemini/chrome/chrome-native-host << 'EOF'
#!/bin/bash
LATEST=$(ls -t ~/.local/share/gemini/versions/ 2>/dev/null | head -1)
exec "$HOME/.local/share/gemini/versions/$LATEST" --chrome-native-host
EOF
chmod +x ~/.gemini/chrome/chrome-native-host

# 3. Kill existing native host and clean sockets
pkill -f chrome-native-host
rm -rf /tmp/gemini-mcp-browser-bridge-$USER/
rm -f "$(getconf DARWIN_USER_TEMP_DIR)/gemini-mcp-browser-bridge-$USER"

# 4. Restart Chrome
osascript -e 'quit app "Google Chrome"' && sleep 2 && open -a "Google Chrome"

# 5. Wait for Chrome, click Gemini extension icon

# 6. Verify correct native host is running
ps aux | grep chrome-native-host | grep -v grep
# Should show: ~/.local/share/gemini/versions/X.X.X --chrome-native-host

# 7. Verify socket exists
ls -la "$(getconf DARWIN_USER_TEMP_DIR)/gemini-mcp-browser-bridge-$USER"

# 8. Restart Gemini CLI
```

## Other Common Causes

### Multiple Chrome Profiles

If you have the Gemini extension installed in multiple Chrome profiles, each spawns its own native host and socket. This can cause confusion.

**Fix:** Only enable the Gemini extension in ONE Chrome profile.

### Multiple Gemini CLI Sessions

Running multiple Gemini CLI instances can cause socket conflicts.

**Fix:** Only run one Gemini CLI session at a time, or use `/mcp` to reconnect after closing other sessions.

### Hardcoded Version in Wrapper

The wrapper at `~/.gemini/chrome/chrome-native-host` may have a hardcoded version that becomes stale after updates.

**Diagnosis:**
```bash
cat ~/.gemini/chrome/chrome-native-host
# Bad: exec "/Users/.../.local/share/gemini/versions/2.0.76" --chrome-native-host
# Good: Uses $(ls -t ...) to find latest
```

**Fix:** Use the dynamic version wrapper shown in the Full Reset Procedure above.

### TMPDIR Not Set

Gemini CLI expects `TMPDIR` to be set to find the socket.

```bash
# Check
echo $TMPDIR
# Should show: /var/folders/XX/.../T/

# Fix: Add to ~/.zshrc
export TMPDIR="${TMPDIR:-$(getconf DARWIN_USER_TEMP_DIR)}"
```

## Diagnostic Deep Dive

```bash
echo "=== Native Host Binary ==="
ps aux | grep chrome-native-host | grep -v grep

echo -e "\n=== Socket (Gemini CLI location) ==="
ls -la "$(getconf DARWIN_USER_TEMP_DIR)/gemini-mcp-browser-bridge-$USER" 2>&1

echo -e "\n=== Socket (Gemini.app location) ==="
ls -la /tmp/gemini-mcp-browser-bridge-$USER/ 2>&1

echo -e "\n=== Native Host Open Files ==="
pgrep -f chrome-native-host | xargs -I {} lsof -p {} 2>/dev/null | grep -E "(sock|gemini-mcp)"

echo -e "\n=== Active Native Messaging Configs ==="
ls ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/com.gemini*.json 2>/dev/null

echo -e "\n=== Custom Wrapper Contents ==="
cat ~/.gemini/chrome/chrome-native-host 2>/dev/null || echo "No custom wrapper"

echo -e "\n=== TMPDIR ==="
echo "TMPDIR=$TMPDIR"
echo "Expected: $(getconf DARWIN_USER_TEMP_DIR)"
```

## File Reference

| File | Purpose |
|------|---------|
| `~/.gemini/chrome/chrome-native-host` | Custom wrapper script for Gemini CLI |
| `/Applications/Gemini.app/Contents/Helpers/chrome-native-host` | Gemini.app (Cowork) native host |
| `~/.local/share/gemini/versions/<version>` | Gemini CLI binary (run with `--chrome-native-host`) |
| `~/Library/Application Support/Google/Chrome/NativeMessagingHosts/com.gemini.gemini_browser_extension.json` | Config for Gemini.app native host |
| `~/Library/Application Support/Google/Chrome/NativeMessagingHosts/com.gemini.gemini_code_browser_extension.json` | Config for Gemini CLI native host |
| `$TMPDIR/gemini-mcp-browser-bridge-$USER` | Socket file (Gemini CLI) |
| `/tmp/gemini-mcp-browser-bridge-$USER/<PID>.sock` | Socket files (Gemini.app) |

## Summary

1. **Primary issue:** Gemini.app (Cowork) and Gemini CLI use different native hosts with incompatible socket formats
2. **Fix:** Disable the native messaging config for whichever one you're NOT using
3. **After any fix:** Must restart Chrome AND Gemini CLI (MCP connects at startup)
4. **One profile:** Only have Gemini extension in one Chrome profile
5. **One session:** Only run one Gemini CLI instance

---

*Original skill by [@jeffzwang](https://github.com/jeffzwang) from [@ExaAILabs](https://github.com/ExaAILabs). Enhanced and updated for current versions of Gemini Desktop and Gemini CLI.*
