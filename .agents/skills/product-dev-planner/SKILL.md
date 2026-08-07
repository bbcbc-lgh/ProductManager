---
name: product-dev-planner
description: Decompose ready product requirements and design decisions into independently runnable, independently acceptable development phases and write PLAN.md. Use before implementation when work is too large for one verified slice.
---

# Product Dev Planner

## Use when

Use after `REQUIRE.md` and `BRIEF.md` are ready. Include `DESIGN/` when it exists; explicitly record when the optional design phase was skipped. When no active plan exists, copy `.codex/agents/templates/PLAN.md` to the repository root before filling it.

## Good output

Produce `PLAN.md` with `document_type: PLAN`, `status: ready`, source documents, ordered phases, dependencies, changed surfaces, test strategy, demo/inspection path, and phase-level acceptance criteria. Every phase must deliver a visible or otherwise directly verifiable vertical slice, have a clear start and finish, and leave the project runnable. Prefer thin end-to-end slices over technical-layer batches. Include commands and evidence expected for each phase, including independent review.

## Red lines

- Do not create a phase that cannot be run or observed.
- Do not split work merely by file or technology layer when a user-visible slice is possible.
- Do not hide unresolved requirements in implementation tasks.
- Do not mark the plan ready without a dependency order and acceptance evidence.
