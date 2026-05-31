---
name: peer-review
description: Use when formally reviewing a scientific manuscript, preprint, grant proposal, or research artifact for rigor and constructive feedback.
---

# Peer Review

Adapted from K-Dense's upstream `peer-review` skill without mandatory visual
asset generation. For ML papers, this incorporates Jakob Foerster's *How to
ML Review - A Brief Guide* and defers to the applicable venue policy.

## Principles

1. Check the venue's reviewer form, confidentiality, anonymity, conflict,
   ethics, and AI-assistance policy. Venue policy overrides this skill.
2. Do not submit a confidential manuscript to an external model or agent when
   the policy forbids it; only proceed through an approved or local route.
3. Identify the paper type and appropriate burden of evidence rather than
   assuming every contribution must achieve state of the art.

## Workflow

1. Skim for the question, claimed contribution, form of paper, methods, and
   main findings. Record what the authors claim before judging it.
2. Read analytically and map each central claim to supporting evidence,
   assumptions, and plausible alternative explanations.
3. Check novelty and significance against relevant literature only where
   needed; cite a concrete prior work when arguing that a claim is not new.
4. Inspect methodology, results, reproducibility, ethics, and the applicable
   reporting or venue requirements.
5. Separate decisive concerns from helpful revisions; each concern should
   identify the location, why it matters, and what evidence or revision could
   resolve it.
6. State a recommendation after the argument, and state what author response
   or bounded additional evidence could change it when applicable.

### Computational/ML Additions

- Check code/data availability, configurations, baselines, tuning fairness,
  leakage, seeds, compute comparability, and whether metrics establish the
  stated claim.
- For empirical methods, ask whether ablations isolate the claimed
  contribution under fair re-tuning and whether conclusions survive suitable
  uncertainty or robustness checks.
- For theoretical work, check assumptions, proof steps, novelty of results,
  and whether experiments are claimed as illustration or validation.
- For datasets, benchmarks, and evaluation work, check provenance,
  documentation, bias/limitations, intended use, and what claims the artifact
  can actually support.
- Use `scientific-critical-thinking` for a focused validity assessment and
  `literature-review` when prior-work coverage or novelty must be checked.

## Output

Write the review to
`<project-dir>/docs/<task-arc>/artifacts/<paper-name>-review.md`.
Keep two levels distinct:

1. **Abstract-level assessment**: claimed question and contribution, paper
   type, significance/originality, evidence sufficiency, and recommendation
   with its decisive reasons.
2. **Concrete assessment**: numbered major issues, numbered minor issues,
   questions for the authors, reproducibility/ethics/policy notes, and
   location-specific corrections or experiments.

Be constructive and specific. Poor language alone is not a rejection reason
unless it prevents evaluation; unsupported claims, technical invalidity, or
missing decisive evidence can be.

## Sources

- Upstream base: K-Dense `peer-review`, retained selectively without unrelated
  schematic generation.
- ML guidance: Jakob N. Foerster, *How to ML Review - A Brief Guide*,
  <https://www.jakobfoerster.com/how-to-review-ml-paper>.
- Venue guidance: ICLR 2026 Reviewer Guide,
  <https://iclr.cc/Conferences/2026/ReviewerGuide>; NeurIPS 2026 Evaluations
  and Datasets Reviewer Guidelines,
  <https://nips.cc/Conferences/2026/EvaluationsDatasetsReviewerGuidelines>.
