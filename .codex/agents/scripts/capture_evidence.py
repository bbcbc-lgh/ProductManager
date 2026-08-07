"""Run one command without a shell and save structured phase evidence."""
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--phase", required=True)
    parser.add_argument("--kind", choices=("build", "test", "acceptance"), required=True)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("a command is required after --")

    root = Path(args.root).resolve()
    result = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
    output = result.stdout + result.stderr
    payload = {
        "phase_id": args.phase,
        "kind": args.kind,
        "command": command,
        "exit_code": result.returncode,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "output": output,
    }
    evidence_dir = root / ".codex" / "agents" / "evidence" / args.phase
    evidence_dir.mkdir(parents=True, exist_ok=True)
    path = evidence_dir / f"{args.kind}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output, end="")
    print(f"\n[evidence] {path.relative_to(root).as_posix()}")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
