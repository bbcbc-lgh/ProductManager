---
name: product-design-brief-builder
description: Interview a product owner about visual and interaction intent, translate subjective preferences into concrete design decisions, and produce a ready BRIEF.md from REQUIRE.md. Use after requirements are ready or when a design direction is still vague.
---

# Product Design Brief Builder

## Use when

Use after `REQUIRE.md` is `ready`, or when an existing product needs an explicit visual system before design or implementation. Present a small set of materially different directions when the user gives a mood word such as premium, calm, technical, playful, or editorial. When no active brief exists, copy `.codex/agents/templates/BRIEF.md` to the repository root before filling it.

## Good output

Produce `BRIEF.md` with `document_type: BRIEF`, `status: ready`, and a traceable source link to `REQUIRE.md`. Convert taste into decisions: audience posture, visual tone, light/dark strategy, density, layout rhythm, typography roles, color semantics, surfaces, motion, responsive behavior, accessibility, content hierarchy, component states, and explicit anti-patterns. Record the chosen direction and rejected alternatives. Every decision should explain which requirement or user preference it serves.

Use [interview-prompts.md](references/interview-prompts.md) for design interviews.

## Red lines

- Do not choose a direction without showing credible alternatives when intent is ambiguous.
- Do not use aesthetic adjectives as if they were specifications.
- Do not override accessibility, legibility, or product constraints for visual novelty.
- Do not mark `ready` while a decision would materially change the implementation and remains unanswered.
