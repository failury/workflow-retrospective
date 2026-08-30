# Workflow Retrospective

`workflow-retrospective` is a Codex and Claude Code skill for finding recurring workflows, repeated mistakes, and avoidable friction in accessible conversation history or supplied artifacts. It proposes the smallest effective improvement: instructions, skills, project rules, scripts, templates, automations, or memory.

It reads full raw turns when they are available, never substitutes chat previews or summaries for a transcript, reports its coverage boundary, and waits for approval before making persistent changes. For repeated errors, it identifies the trigger, failure mode, and a targeted prevention.

## Install

```bash
npx skills add failury/workflow-retrospective
```

To target a specific agent:

```bash
npx skills add failury/workflow-retrospective --agent codex
npx skills add failury/workflow-retrospective --agent claude-code
```

## Included helper

The helpers use only the Python standard library:

- `scripts/normalize_chatgpt_export.py` converts ChatGPT export JSON into raw-message JSONL.
- `scripts/normalize_codex_export.py` converts Codex rollout JSONL files or session directories into a complete normalized raw-record stream.
- `scripts/normalize_claude_code_export.py` converts a Claude Code transcript JSONL file or project transcript directory into a complete normalized raw-record stream, retaining tool-use and tool-result records.

## Status

The skill is tested locally and released under the [MIT License](LICENSE).
