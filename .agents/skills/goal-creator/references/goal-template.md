# Goal: <specific outcome>

```yaml
goal_id: <phase-or-task-id>
objective: <one bounded result>
inputs:
  - <repository-relative path>
completion_criteria:
  - <observable condition>
acceptance_evidence:
  - <command output or artifact path>
gate_command: python .codex/agents/scripts/workflow_gate.py --phase <phase-id>
state: active
```

## Execution loop

Continue implementation, verification, independent review, and correction until every criterion has evidence and the gate exits successfully.
