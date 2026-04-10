#!/usr/bin/env python3
import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

DEFAULT_SINK = Path.home() / ".gemini" / "skill_traces.jsonl"

class TraceLogger:
    def __init__(self, sink_path: Path = DEFAULT_SINK):
        self.sink_path = sink_path
        self.sink_path.parent.mkdir(parents=True, exist_ok=True)

    def log_trace(
        self,
        skill_name: str,
        user_prompt: str,
        trajectory: List[Dict[str, Any]],
        final_response: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Path:
        """Logs a single agent execution trace to the JSONL sink."""
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "skill_name": skill_name,
            "user_prompt": user_prompt,
            "trajectory": trajectory,
            "final_response": final_response,
            "metadata": metadata or {},
            "evaluated": False,
            "evaluation_result": None
        }
        
        with open(self.sink_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")
            
        return self.sink_path

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Log an agent execution trace.")
    parser.add_argument("--skill", required=True, help="Name of the skill used")
    parser.add_argument("--prompt", required=True, help="The user prompt")
    parser.add_argument("--response", required=True, help="The final agent response")
    parser.add_argument("--trajectory", help="JSON string of tool calls/results")
    
    args = parser.parse_args()
    
    traj = json.loads(args.trajectory) if args.trajectory else []
    
    logger = TraceLogger()
    path = logger.log_trace(args.skill, args.prompt, traj, args.response)
    print(f"Trace logged to {path}")
