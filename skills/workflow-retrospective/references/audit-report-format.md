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

For recommendations, add a short paragraph covering independent recurrence, impact if repeated, the proposed destination, scope, benefit, safety/authority boundary, overlap check, and a draft outline if approval would make implementation straightforward.

## Do not standardize

List credible near-misses and why they remain ad hoc, such as low recurrence, temporary context, excessive variability, or obsolete tooling.

## Next approval

Provide a small numbered set of independently approvable actions. Do not implement them as part of the audit.
