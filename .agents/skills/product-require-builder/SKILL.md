---
name: product-require-builder
description: Turn an ambiguous product idea into a development-ready REQUIRE.md through direct, non-flattering questioning. Use when a product is new, its scope is unclear, or downstream design and planning lack testable requirements.
---

# Product Require Builder

## Use when

Use for a new product idea, a major feature with unclear boundaries, or a requirements document that cannot yet drive implementation. Read the user's source material and any existing `REQUIRE.md` before asking questions. When no active document exists, copy `.codex/agents/templates/REQUIRE.md` to the repository root before filling it.

## Good output

Produce a UTF-8 `REQUIRE.md` with `document_type: REQUIRE`, `status: ready`, version, source documents, and no unresolved blocking questions. It must define the problem, target users, primary journeys, in-scope and out-of-scope behavior, domain/data constraints, non-functional requirements, risks, priorities, and observable acceptance criteria. Each requirement must be testable or explicitly marked as a product decision still needed.

Interview until the next agent can build a thin, runnable vertical slice without inventing product behavior. Challenge contradictions, vanity features, unsupported assumptions, and missing ownership. Say what is unknown instead of filling gaps with praise.

Use [question-bank.md](references/question-bank.md) when the initial idea is underspecified.

## Red lines

- Do not write `ready` while a blocking product decision is unresolved.
- Do not turn implementation guesses into requirements.
- Do not promise business outcomes that have no observable measure.
- Do not silently expand scope to make the idea sound impressive.
