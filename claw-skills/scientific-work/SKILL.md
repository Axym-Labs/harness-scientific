---
name: scientific-work
description: Use when planning, executing, reviewing, or interpreting scientific or ML work intended to support a knowledge claim.
---

# Scientific Work

Scientific automation should produce reliable insight, not merely completed
runs or improved metrics. Claw retains responsibility for the question,
experimental validity, interpretation, and claims even when implementation is
delegated.

## Protocol

1. Define the question and mode: bounded engineering optimization, controlled
   hypothesis test, exploratory evidence gathering, or potential publishable
   claim.
2. Establish why an answer is valuable. Use `literature-review` to ground
   state-of-the-art or novelty claims.
3. State hypotheses, baselines, controls, metrics, confounders, failure
   conditions, and stopping criteria before decisive experiments.
4. Use `research` for sourced evidence, `test-hypothesis` for controlled
   comparisons, and `scientific-critical-thinking` when assessing evidence or
   conclusions.
5. Validate that implemented experiments match the intended intervention
   before interpreting measurements.
6. Analyze alternatives, negative results, sensitivity, and whether a metric
   change answers the actual question.
7. Separate observed evidence, interpretation, uncertainty, and recommendation
   in the deliverable.

## Judgment Gates

- Do not silently change the research question after results arrive.
- Seek a decision before committing substantial resources to a new direction
  or presenting a consequential claim as established.
- Do not describe a successful run or plausible narrative as scientific
  progress without evidence for the underlying claim.

Read `references/failure-modes.md` for open-ended or autonomous-looking work.
