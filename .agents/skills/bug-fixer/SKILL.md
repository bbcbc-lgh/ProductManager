---
name: bug-fixer
description: Reproduce, isolate, fix, and verify a reported software bug with minimal scope. Use when behavior is incorrect, a regression is suspected, or a failing test needs a root-cause fix.
---

# Bug Fixer

## Use when

Use when a bug report, failing test, crash, or regression exists. Establish the expected and observed behavior before editing.

## Good output

Create or identify a reliable reproduction, explain the root cause, add or update a regression test, make the smallest fix, and run relevant verification. Record residual risk and affected scope. Use `code-reviewer` for an independent review when the fix changes shared behavior or the project workflow requires it.

## Red lines

- Do not "fix" a symptom by weakening a test or hiding an error.
- Do not expand a bug fix into unrelated refactoring.
- Do not declare success without a reproduction that now passes or a documented environmental blocker.
