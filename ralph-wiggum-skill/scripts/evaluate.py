#!/usr/bin/env python3
import sys
import os

def evaluate():
    print(f"Evaluating {os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))} skill...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    required_files = ["SKILL.md"]
    for file in required_files:
        if not os.path.exists(os.path.join(base_dir, file)):
            print(f"Error: Missing required file {file}")
            return 1
    print("Evaluation complete. All checks passed.")
    return 0

if __name__ == "__main__":
    sys.exit(evaluate())
