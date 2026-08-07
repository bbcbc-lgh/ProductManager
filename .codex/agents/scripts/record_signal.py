"""Append one structured user-feedback signal without editing durable rules."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--source", choices=("user_feedback", "correction", "rejection", "praise"), required=True)
    parser.add_argument("--feedback", required=True)
    parser.add_argument("--context", required=True)
    parser.add_argument("--observed", required=True)
    parser.add_argument("--desired", required=True)
    parser.add_argument("--area", required=True)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    signal_dir = root / ".codex" / "evolution" / "signals"
    signal_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    signal_id = f"{now:%Y%m%dT%H%M%SZ}-{uuid4().hex[:8]}"
    payload = {
        "signal_id": signal_id,
        "recorded_at": now.isoformat(),
        "source": args.source,
        "raw_feedback": args.feedback,
        "context": args.context,
        "observed_behavior": args.observed,
        "desired_behavior": args.desired,
        "candidate_rule_area": args.area,
        "repeat_count": 1,
        "state": "new",
    }
    output = signal_dir / f"{signal_id}.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output.relative_to(root).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
