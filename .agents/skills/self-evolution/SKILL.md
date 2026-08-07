---
name: self-evolution
description: Turn accumulated user corrections and rejected behavior into reviewable rule-change proposals, including deletion of rules that are stale or never useful. Use at the start of a new Desktop conversation or when the user asks to improve the workflow rules.
---

# Self Evolution

## Use when

Read `.codex/EVOLUTION.md`, `.codex/evolution/signals/`, `.codex/evolution/state.json`, current `AGENTS.md`, and relevant skills when the `SessionStart` hook reports unprocessed signals or when the user asks for evolution. Use exactly one clean-context subagent governed by `.codex/agents/evolution-analyst.md`; the primary agent must inspect its evidence and present the proposal to the user.

## Good output

Create a proposal under `.codex/evolution/proposals/` that groups repeated signals, distinguishes preferences from one-off incidents, identifies contradictions, and proposes precise additions, edits, or deletions. Cite signal IDs and affected files. Ask for explicit approval item by item. After approval, update only the accepted rules, signal states, and `.codex/evolution/state.json`.

## Red lines

- Do not auto-edit durable rules from raw criticism.
- Do not turn every complaint into a permanent rule.
- Do not accumulate rules that duplicate or contradict existing guidance.
- Do not delete a rule without showing why it is obsolete or never useful.
