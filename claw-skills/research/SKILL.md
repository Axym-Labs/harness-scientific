---
name: research
description: Use when gathering sourced evidence about a question and producing a durable research deliverable.
---

# Research

## Workflow

1. Read `$VAULT_PATH/Agent/Task Skills/research.md` when it exists.
2. Define the question, scope (`quick` or `deep`), decision it informs, and
   what evidence could change the conclusion.
3. Prefer primary sources for factual or technical claims; record external
   links and relevant publication dates.
4. For a research claim load `scientific-work`; for a broad prior-work survey
   load `literature-review`; for a controlled comparison load `test-hypothesis`.
5. Execute directly or delegate collection/analysis with an explicit question,
   source requirements, and output contract.
6. Write useful durable results to
   `$VAULT_PATH/Knowledge/research/YYYY-MM-DD_topic.md` and log a concise
   reference in `$VAULT_PATH/Agent/Memory/research-log.md`.

## Output

Include the question and scope, short answer, evidence and sources, explicit
inferences or beliefs, unresolved uncertainty, and supported next step.

## Rules

- Do not present inference as sourced fact.
- Do not create notes to fill a log or duplicate existing vault material.
- In `DRY_RUN`, do not perform outward-facing actions or launch paid work just
  to test the workflow.
