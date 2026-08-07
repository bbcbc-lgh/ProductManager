"""Inject startup context only when unprocessed feedback signals exist."""
from __future__ import annotations

import json
from pathlib import Path


def find_project_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / "AGENTS.md").is_file() and (candidate / ".codex").is_dir():
            return candidate
    return start


def main() -> None:
    root = find_project_root(Path.cwd().resolve())
    signal_dir = root / ".codex" / "evolution" / "signals"
    pending = []
    if signal_dir.is_dir():
        for path in sorted(signal_dir.glob("*.json")):
            try:
                signal = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if signal.get("state") == "new":
                pending.append(path.relative_to(root).as_posix())
    if not pending:
        return
    context = (
        f"Found {len(pending)} unprocessed workflow feedback signal(s): "
        + ", ".join(pending[:20])
        + ". Before normal project work, dispatch exactly one clean-context subagent "
        "using .codex/agents/evolution-analyst.md and $self-evolution to analyze "
        "these signals and current durable rules. "
        "The primary agent must present proposed additions, edits, and deletions to "
        "the user one by one; do not apply any proposal without explicit approval."
    )
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": context,
                }
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
