# codex retrospec

`workflow-retrospective` is a Codex-native skill for auditing accessible conversation history or supplied artifacts for genuinely recurring workflows, then proposing the smallest reusable form: instructions, skills, project rules, scripts, templates, automations, or memory.

It reads full raw turns when they are available, never substitutes chat previews or summaries for a transcript, reports its coverage boundary, and waits for approval before making persistent changes.

## Install

```bash
npx skills add failury/codex-retrospec
```

## Included helper

`scripts/normalize_chatgpt_export.py` converts ChatGPT export JSON into raw-message JSONL using only the Python standard library.

## Status

The skill is tested locally. A license has not yet been selected for this repository.
