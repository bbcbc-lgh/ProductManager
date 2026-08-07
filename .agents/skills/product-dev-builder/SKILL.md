---
name: product-dev-builder
description: Implement one accepted PLAN.md phase at a time as the primary agent, keeping each slice runnable and verified. Use for planned product development when requirements, design, and phase acceptance criteria are available.
---

# Product Dev Builder

## Use when

Use with a `PLAN.md` phase whose inputs are ready. Before editing, read the relevant requirements, brief/design decisions, existing code conventions, and the phase's acceptance evidence.

## Good output

Implement the smallest complete vertical slice and leave an inspectable result. Capture build, test, and acceptance commands with `.codex/agents/scripts/capture_evidence.py`. Then dispatch one clean-context subagent with `.codex/agents/code-reviewer.md` and the `code-reviewer` skill, containing the phase contract, diff, commands, and outputs. Store the review result at `.codex/agents/reviews/<phase-id>.yaml`. Iterate on every blocking finding and rerun the checks until the structured verdict is `PASS`. Run `.codex/agents/scripts/workflow_gate.py --phase <phase-id>` before declaring the Goal complete.

Parallel delegation is allowed only when work boundaries are independent and the context packet is complete; the primary agent merges and decides.

## Red lines

- Do not claim completion from code generation alone.
- Do not review your own work as the independent verdict.
- Do not bypass a failing test, build, gate, or blocking review finding.
- Do not implement behavior absent from the current phase without recording the scope decision.
