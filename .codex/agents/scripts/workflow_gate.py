"""Mechanical gate for canonical documents, phase evidence, and review verdicts."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def parse_scalar(value: str) -> object:
    value = value.strip()
    if value in {"null", "~"}:
        return None
    if value in {"true", "false"}:
        return value == "true"
    if value.startswith("[") or value.startswith("{"):
        return json.loads(value)
    if value.isdigit():
        return int(value)
    return value.strip('"\'')


def parse_simple_yaml(lines: list[str]) -> dict[str, object]:
    """Parse the flat scalars and block lists used by workflow contracts."""
    data: dict[str, object] = {}
    current_list: list[object] | None = None
    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("-") and current_list is not None:
            current_list.append(parse_scalar(stripped[1:].strip()))
            continue
        if ":" not in stripped:
            continue
        key, raw_value = stripped.split(":", 1)
        if raw_value.strip():
            data[key] = parse_scalar(raw_value)
            current_list = None
        else:
            current_list = []
            data[key] = current_list
    return data


def read_markdown_frontmatter(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening frontmatter delimiter")
    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration as exc:
        raise ValueError("missing closing frontmatter delimiter") from exc
    return parse_simple_yaml(lines[1:end])


def read_yaml(path: Path) -> dict[str, object]:
    return parse_simple_yaml(path.read_text(encoding="utf-8").splitlines())


def require_file(root: Path, relative: str, errors: list[str]) -> Path | None:
    path = root / relative
    if not path.is_file():
        errors.append(f"missing: {relative}")
        return None
    return path


def check_document(root: Path, relative: str, expected_type: str, errors: list[str]) -> None:
    path = require_file(root, relative, errors)
    if not path:
        return
    try:
        data = read_markdown_frontmatter(path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors.append(f"{relative}: invalid frontmatter: {exc}")
        return
    required = ("document_type", "status", "version", "source_documents", "open_questions", "acceptance_criteria")
    for field in required:
        if field not in data:
            errors.append(f"{relative}: missing field {field}")
    if data.get("document_type") != expected_type:
        errors.append(f"{relative}: expected document_type {expected_type}")
    if data.get("status") != "ready":
        errors.append(f"{relative}: status is not ready")
    questions = data.get("open_questions")
    if not isinstance(questions, list):
        errors.append(f"{relative}: open_questions must be a list")
    elif questions:
        errors.append(f"{relative}: unresolved open_questions remain")
    criteria = data.get("acceptance_criteria")
    if not isinstance(criteria, list) or not criteria:
        errors.append(f"{relative}: acceptance_criteria must be a non-empty list")


def check_evidence(root: Path, phase_id: str, errors: list[str]) -> None:
    for kind in ("build", "test", "acceptance"):
        relative = f".codex/agents/evidence/{phase_id}/{kind}.json"
        path = require_file(root, relative, errors)
        if not path:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{relative}: invalid JSON: {exc}")
            continue
        if data.get("exit_code") != 0:
            errors.append(f"{relative}: exit_code is not 0")
        if not data.get("command"):
            errors.append(f"{relative}: command is empty")
        if "output" not in data:
            errors.append(f"{relative}: output is missing")


def check_review(root: Path, phase_id: str, errors: list[str]) -> None:
    relative = f".codex/agents/reviews/{phase_id}.yaml"
    path = require_file(root, relative, errors)
    if not path:
        return
    try:
        data = read_yaml(path)
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{relative}: invalid data: {exc}")
        return
    if data.get("verdict") != "PASS":
        errors.append(f"review {phase_id}: verdict is not PASS")
    for field in ("reviewer", "scope", "evidence", "reviewed_at"):
        if not data.get(field):
            errors.append(f"review {phase_id}: {field} is empty")
    blocking = data.get("blocking_findings")
    if not isinstance(blocking, list):
        errors.append(f"review {phase_id}: blocking_findings must be a list")
    elif blocking:
        errors.append(f"review {phase_id}: blocking findings remain")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--phase", help="Phase id, e.g. P01")
    parser.add_argument("--documents", action="store_true", help="Check REQUIRE, BRIEF, and PLAN")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors: list[str] = []
    if args.documents or args.phase:
        check_document(root, "REQUIRE.md", "REQUIRE", errors)
        check_document(root, "BRIEF.md", "BRIEF", errors)
        check_document(root, "PLAN.md", "PLAN", errors)
    if args.phase:
        check_evidence(root, args.phase, errors)
        check_review(root, args.phase, errors)
    result = {"ok": not errors, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
