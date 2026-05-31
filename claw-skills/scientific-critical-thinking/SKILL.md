---
name: scientific-critical-thinking
description: Use when evaluating scientific evidence, experimental design, validity, confounding, or the strength of a research or ML claim.
---

# Scientific Critical Thinking

Adapted from K-Dense's upstream `scientific-critical-thinking` skill for
Claw's focused research workflow.

## Workflow

1. Identify the precise claim and whether it is descriptive, predictive,
   causal, mechanistic, or a contribution/novelty claim.
2. Check construct validity: do the measurements answer that claim, or only
   move a proxy?
3. Check internal validity: baseline, controls, leakage, confounders,
   intervention fidelity, repeated trials or uncertainty, and changed
   conditions.
4. Check external validity: dataset, domain, hardware/runtime, population, and
   whether conclusions generalize beyond the observed setting.
5. Check reporting validity: negative results, alternate explanations, prior
   work, and separation of evidence from interpretation.
6. Grade the conclusion as supported, suggestive, inconclusive, or unsupported
   and state what would most efficiently distinguish remaining explanations.

### ML-Specific Checks

- Confirm splits, evaluation procedure, seeds/variance, baseline fairness, and
  whether tuning information leaks into comparison.
- Confirm a speed, loss, or benchmark gain corresponds to the actual research
  question and practical constraint.
- Inspect implementation and configuration before attributing results to a
  proposed mechanism.

Do not add generated figures, extra tools, or claims merely because an
upstream workflow suggests them; include only what serves the investigation.
