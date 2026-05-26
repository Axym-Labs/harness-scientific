---
name: scientific-work
description: Use when planning, executing, reviewing, or interpreting scientific or ML work intended to support a knowledge claim.
---

# Scientific Work

Scientific automation should produce reliable insight, not merely completed
runs or improved metrics. Claw retains responsibility for the question,
experimental validity, interpretation, and claims even when implementation is
delegated.

## Value And Hidden Constraints

For a proposed research direction, ask whether it offers contribution,
insight, utility, or novelty, and what evidence would establish that value.
Surface constraints that may invalidate an otherwise attractive result,
including latency, compute or data cost, memory, deployment compatibility,
safety, and whether downstream work requires exact rather than approximate
behavior. Record material constraints in the project spec or exploration note.

## Protocol

1. Define the question and mode: bounded engineering optimization, controlled
   hypothesis test, exploratory evidence gathering, or potential publishable
   claim.
2. Establish why an answer is valuable. Use `scientific-brainstorming` for
   broad direction-finding and `literature-review` to ground state-of-the-art
   or novelty claims.
3. State hypotheses, baselines, controls, metrics, confounders, failure
   conditions, and stopping criteria before decisive experiments.
4. Use `research` or `research-lookup` for sourced evidence,
   `exploratory-data-analysis` before treating patterns as hypotheses,
   `hypothesis-generation` for competing explanations, `test-hypothesis` for
   controlled comparisons, `statistical-analysis` for quantitative inference,
   and `scientific-critical-thinking` when assessing evidence or conclusions.
5. Validate that implemented experiments match the intended intervention
   before interpreting measurements.
6. Analyze alternatives, negative results, sensitivity, and whether a metric
   change answers the actual question.
7. Separate observed evidence, interpretation, uncertainty, and recommendation
   in the deliverable. Use `scientific-writing`, `scientific-visualization`,
   or `scientific-schematics` only when the output needs them.
8. Keep project reports, figures, exports, and agent-produced artifacts under
   the project's `docs/artifacts/`; use the vault for structured knowledge and
   links to those artifacts.

## Judgment Gates

- Do not silently change the research question after results arrive.
- Do not present a recombination of familiar ideas as novel without checking
  prior work.
- Do not interpret measurements until implementation fidelity, baselines,
  controls, confounders, and proxy-to-question fit have been checked.
- Do not replace missing domain knowledge or tacit constraints with a
  confident narrative; state assumptions and seek relevant review.
- Seek a decision before committing substantial resources to a new direction
  or presenting a consequential claim as established.
- Do not describe a successful run or plausible narrative as scientific
  progress without evidence for the underlying claim.

Read `references/failure-modes.md` before nontrivial open-ended research,
autonomous-looking work, or any consequential research claim.
