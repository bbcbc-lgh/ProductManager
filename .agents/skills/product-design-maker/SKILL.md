---
name: product-design-maker
description: Create a complete visual design direction and high-fidelity prototype artifacts from REQUIRE.md and BRIEF.md. Use optionally after the design brief when the product benefits from visual validation before planning or development.
---

# Product Design Maker

## Use when

Use only when the user opts into visual design. Require `REQUIRE.md` and `BRIEF.md` to be `ready`. Inspect existing brand assets and the target platform before selecting prototype formats. Start `DESIGN/DESIGN.md` from `.codex/agents/templates/DESIGN.md`.

## Good output

Create `DESIGN/DESIGN.md`, `DESIGN/images/`, and `DESIGN/prototypes/`. The design document maps screens and states to requirements and brief decisions, names interaction states and responsive behavior, and records assets and open risks. Prototypes may be HTML/CSS, a runnable frontend slice, images, annotated screenshots, or another inspectable format appropriate to the product. Make the primary journey inspectable rather than producing only mood boards. Keep all generated assets referenced from the design document.

## Red lines

- Do not invent flows that contradict `REQUIRE.md`.
- Do not hide missing states behind polished mockups.
- Do not replace a runnable or inspectable artifact with prose alone.
- Do not make visual polish a reason to bypass accessibility or acceptance criteria.
