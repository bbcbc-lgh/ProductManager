---
name: goal-creator
description: Convert current workflow context into a precise executable Goal with measurable completion criteria and evidence-based acceptance. Use when the next action or finish condition is ambiguous, or before driving a phase to completion.
---

# Goal Creator

## Use when

Use with the current phase, source documents, project commands, and review policy. Read the relevant `PLAN.md` slice and existing evidence before writing the Goal.

## Good output

Write a Goal containing one objective, explicit inputs, testable completion criteria, acceptance evidence, a gate command, and a state. Criteria must be observable and scoped to the current phase. Include build/test/review evidence where applicable. The Goal must tell the primary agent what loop to run, not merely what feature sounds desirable. When the Desktop Goal capability is available, call it with the finished objective so execution begins; do not stop after showing a draft. When the mechanical gate needs a repository manifest, create it from `.codex/agents/templates/GOAL.yaml` under `.codex/agents/goals/`.

## Red lines

- Do not use vague verbs such as improve, polish, or finish without a measure.
- Do not define acceptance evidence that the project cannot produce.
- Do not make a Goal complete because the agent ran out of time or context.
- Do not silently change the phase scope to make the Goal easier.
