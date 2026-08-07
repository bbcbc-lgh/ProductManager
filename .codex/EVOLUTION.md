# Evolution Contract

Self-evolution converts user feedback into explicit, reviewable changes without allowing rules to grow without bound.

## Signal lifecycle

Record a signal when the user corrects, rejects, or criticizes agent behavior. Store raw signals as JSON in `.codex/evolution/signals/`; do not reinterpret the user's words while recording them. A signal begins in `state: new`.

At session startup, the hook checks only for new signals. If any exist, the primary agent dispatches one clean-context subagent using `.codex/agents/evolution-analyst.md` and the `self-evolution` skill. Store its proposal in `.codex/evolution/proposals/`.

The primary agent presents each proposed addition, edit, or deletion separately. Only explicit user approval authorizes a durable rule change. After a decision, update the signal state and `.codex/evolution/state.json`.

## Quality bar

A proposal is useful only when it cites source signal IDs, identifies the affected rule, gives exact replacement text, explains expected impact, and checks for duplication or contradiction. Prefer editing an existing rule to adding another. Propose deletion when a rule is obsolete, duplicated, contradicted by stronger evidence, or repeatedly irrelevant.

## Red lines

- Never turn praise, frustration, or a one-off exception directly into a durable rule.
- Never modify `AGENTS.md` or `.agents/skills/` before user approval.
- Never erase raw feedback when a proposal is rejected; retain its decision state.
- Never use evolution to relax mechanical gates or security controls merely to finish a task.
