#!/bin/bash
# Daily Skill Evolution and Sync Pipeline

EVOLUTION_DIR="$HOME/my-skills/.gemini/evolution"
ANTIGRAVITY_SYNC="$HOME/.gemini/antigravity/global_skills/sync_skills.sh"

echo "=== Starting Daily Skill Maintenance: $(date) ==="

if [ -d "$EVOLUTION_DIR" ]; then
    echo "1. Running Trace Evaluation..."
    "$EVOLUTION_DIR/evaluate_traces.py"
    
    echo "2. Running Skill Evolution (Gemini 3)..."
    "$EVOLUTION_DIR/evolve_skills.py"
else
    echo "Error: Evolution directory not found."
    exit 1
fi

if [ -f "$ANTIGRAVITY_SYNC" ]; then
    echo "3. Syncing to Antigravity..."
    bash "$ANTIGRAVITY_SYNC"
else
    echo "Warning: Antigravity sync script not found."
fi

echo "=== Maintenance Complete: $(date) ==="
