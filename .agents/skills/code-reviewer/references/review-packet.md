# Review Packet Contract

The primary agent provides:

- phase ID and acceptance criteria;
- relevant excerpts or paths from REQUIRE.md, BRIEF.md, DESIGN/, and PLAN.md;
- changed-file list and diff;
- build, lint, and test commands with outputs;
- known risks and explicit out-of-scope items;
- destination path `.codex/agents/reviews/<phase-id>.yaml`.

The reviewer returns findings first, then a structured verdict matching `.codex/agents/schemas/review.schema.yaml`.
