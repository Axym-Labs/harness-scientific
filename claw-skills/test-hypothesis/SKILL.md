---
name: test-hypothesis
description: Use when answering one empirical question with a baseline and one controlled intervention.
---

# Test Hypothesis

One hypothesis, one controlled intervention, one evidence-bounded conclusion.

## Procedure

1. State a falsifiable hypothesis before running the experiment.
2. Specify the dependent metric, baseline, controlled variables, expected
   confounders, repetitions or variance handling, and failure criteria.
3. Measure the baseline reproducibly and record environment details that
   plausibly affect the result.
4. Apply one intervention. Inspect implementation/configuration to confirm it
   is the intended change.
5. Repeat the measurement comparably and report raw result, delta, and
   uncertainty.
6. Conclude `supported`, `rejected`, or `inconclusive`; state limitations and
   alternative explanations.

## Rules

- A missing baseline or changed measurement procedure invalidates a causal
  comparison.
- Negative and inconclusive results are results; report them.
- A proxy metric gain does not by itself establish the broader claim.
- Log material experiments in `$VAULT_PATH/Agent/Memory/experiments.md`
  without filling it with trivial checks.

For open-ended research direction or publishable interpretation also load
`scientific-work` and, when assessing conclusions, `scientific-critical-thinking`.
