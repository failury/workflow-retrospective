# Audit report format

Use this structure when a full retrospective is requested. Scale it down for a focused review.

## Coverage

- Sources reviewed, with kind and workspace/repository scope
- Files, bytes, raw records, independent root sessions, and date range, when knowable
- Raw-turn retrieval method and whether every selected source reached its final page or EOF
- Exclusion rules and counts, including injected instructions, skill definitions, approval transcripts, and fork/sidechain duplicates
- Malformed, inaccessible, or explicitly truncated record count
- Limitations and inaccessible sources

## Findings

Use one compact entry per candidate:

| Pattern | Evidence and independent roots | Scope | Classification | Recommendation | Confidence |
|---|---|---|---|---|

For recommendations, add a short paragraph covering independent recurrence, impact if repeated, the proposed destination, scope, benefit, safety/authority boundary, and overlap check.

## Do not standardize

List credible near-misses and why they remain ad hoc, such as low recurrence, temporary context, excessive variability, or obsolete tooling.

## Next approval

For each item, use this structure before asking for approval:

### Proposal: `<short action name>`

- **Operation:** Create or update
- **Target:** Exact artifact path or existing skill name and path
- **Scope:** Personal, workspace, repository, or product/platform
- **Reason:** One concise evidence-backed sentence

Show exact content immediately below the metadata:

- Existing files: a unified diff with enough surrounding context to review the change.
- New `AGENTS.md`: the complete initial file content.
- New skill: the destination directory, every file to create, the complete `SKILL.md`, and every supporting-file content.

End with a small numbered set of independently approvable proposals. Do not implement any of them as part of the audit, and do not make a material change beyond the preview without renewed approval.
