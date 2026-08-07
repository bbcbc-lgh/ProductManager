# Codex Product Workflow

This repository uses one primary agent as the owner of the product workflow. The primary agent may delegate only (a) clean-context independent review or (b) explicitly parallel work with a complete context packet. It must merge results and make the final decision.

## Workflow contract

Use these artifacts as phase interfaces:

`REQUIRE.md` -> `BRIEF.md` -> optional `DESIGN/` -> `PLAN.md` -> implementation, tests, review -> release audit and package.

Do not advance a phase when its input artifact is missing, has `status: draft`, contains unresolved blocking questions, or fails the repository gate. Do not silently rewrite an upstream artifact to make downstream work fit; record a change request and ask the user when the product decision changes.

The optional design phase may be skipped. When it is skipped, `product-dev-planner` must record that the plan is based on `REQUIRE.md` and `BRIEF.md` only.

## Operating posture

- Ask direct questions when the idea, priority, scope, or acceptance condition is vague. Do not flatter the user or pretend an assumption is a decision.
- Keep each phase independently runnable and demonstrable. A phase is not complete if it only creates invisible infrastructure.
- Prefer the smallest implementation that satisfies the current phase. Do not add speculative flexibility.
- Treat `REQUIRE.md`, `BRIEF.md`, and `PLAN.md` as versioned contracts. Preserve decisions and list open questions explicitly.
- Keep procedural detail in the relevant skill. Keep this file limited to durable repository behavior.

## Gates and evidence

Use `.codex/agents/scripts/workflow_gate.py` for mechanical checks. A gate may inspect files, schemas, command results, and structured review verdicts; it must not replace human/product judgment.

For implementation phases, the required evidence is:

1. the phase acceptance result;
2. build, lint, and test output appropriate to the project;
3. an independent review record at `.codex/agents/reviews/<phase-id>.yaml` with `verdict: PASS`;
4. a clean gate result.

The primary agent must not mark a Goal complete while the gate is non-zero or the review verdict is not `PASS`.

## Delegation protocol

Before delegating, select the matching contract under `.codex/agents/`: `code-reviewer.md`, `evolution-analyst.md`, or `parallel-worker.md`. Write a context packet containing the relevant requirements, plan slice, changed paths or work boundary, commands to run, and the exact return schema. The delegate must return findings or artifacts, not a vague summary. The primary agent owns merge conflicts, tradeoffs, and final acceptance.

## Feedback and evolution

When the user corrects, rejects, or criticizes behavior, append a signal under `.codex/evolution/signals/` using `.codex/agents/scripts/record_signal.py`. Follow `.codex/EVOLUTION.md`. Do not directly mutate rules during a working task. `self-evolution` may prepare a proposal, but only explicit user approval may change `AGENTS.md` or a skill. Prefer modifying or deleting stale rules over accumulating rules.

At conversation startup, honor the `SessionStart` context from `.codex/hooks/session_start.py`. When it reports unprocessed signals, dispatch exactly one clean-context subagent with `self-evolution`; give it the signals and current durable rules, then let the primary agent present and decide how to merge its proposals. Do not dispatch when no unprocessed signal exists.

## Goal execution

Start meaningful work from a Goal with an objective, measurable completion criteria, and evidence-based acceptance. Use `goal-creator` when any of these are missing or ambiguous. A Goal is complete only when its acceptance evidence is present and the relevant gate passes.

When the Desktop Goal capability is available, create the Goal there after drafting it; do not stop at a Markdown draft. Keep a repository Goal manifest only when a gate needs machine-readable criteria.

## Skill authoring

Use Codex's built-in `$skill-creator` for creating or updating workflow skills. Store project workflow skills under `.agents/skills/`. Do not create a project-local skill named `skill-creator`; that name is reserved for the built-in skill.

## Desktop-first scope

This package targets Codex Desktop behavior first. CLI-specific launchers and automation are intentionally out of scope for this version. Project-local scripts remain portable where practical, but Desktop is the acceptance surface.

## Artifact status

Canonical documents use the YAML fields described in `.codex/agents/schemas/`. Starter documents live in `.codex/agents/templates/`; copy them to the repository root only when the corresponding phase starts. Allowed status values are `draft`, `ready`, and `superseded`. Use UTF-8 Markdown and keep generated evidence paths relative to the repository root.
