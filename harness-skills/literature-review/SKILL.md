---
name: literature-review
description: Use when systematically surveying prior work, synthesizing research evidence, or establishing the state of the art for a scientific question.
---

# Literature Review

Adapted from K-Dense's upstream `literature-review` skill without requiring a
particular paid backend or generated visual assets.

## Workflow

1. Define the research question, intended decision, review type, scope, date
   limits, and inclusion/exclusion rules.
2. Build search terms and identify suitable primary databases or repositories
   for the domain, such as arXiv, Semantic Scholar, PubMed, ACM, or IEEE.
3. Record search strings, search dates, result counts where available, and
   screening decisions sufficiently for reproducibility.
4. Read and cite primary papers for material claims; use reviews for mapping
   the field and locating primary evidence.
5. Synthesize themes, disagreements, missing evidence, and apparent gaps.
   Distinguish an unstudied question from a well-tested dead end.
6. Verify citation identity and relevance before saving the deliverable.

## Output

Include question/scope, search method, selected evidence, synthesis, limits,
open questions, and external links. For a new scientific direction, hand the
result to `scientific-work` before framing novelty or experiments.
When the review is a project deliverable, store it under
`<task-arc-dir>/artifacts/`; reserve vault notes for durable linked knowledge.

Do not create diagrams or invoke external services unless they are useful to
the deliverable and available under the current tool/credential policy.
