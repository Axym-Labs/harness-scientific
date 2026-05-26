---
name: research
description: Use when gathering sourced evidence about a question and producing a durable research deliverable.
---

# Research

## Workflow

1. Define the question, scope (`quick` or `deep`), decision it informs, and
   what evidence could change the conclusion.
2. Prefer primary sources for factual or technical claims; record external
   links and relevant publication dates.
3. For a research claim load `scientific-work`; for a broad prior-work survey
   load `literature-review`; for a controlled comparison load `test-hypothesis`.
4. Execute directly or, when delegating collection/analysis, load
   `supervising` and dispatch with an explicit question, source
   requirements, output contract, and acceptance check.
5. For durable results, use `capture-knowledge` to write or update a linked
   note under `$VAULT_PATH/Knowledge/research/`.
6. Store project-specific reports, exports, figures, and other produced
   artifacts under the project's `docs/artifacts/`, linking to them from a
   knowledge note when useful.

## Output

Include the question and scope, short answer, evidence and sources, explicit
inferences or beliefs, unresolved uncertainty, and supported next step.

## Rules

- Do not present inference as sourced fact.
- Do not create notes to fill a log or duplicate existing vault material.
- In `DRY_RUN`, do not perform outward-facing actions or launch paid work just
  to test the workflow.
