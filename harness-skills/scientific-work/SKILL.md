---
name: scientific-work
description: Use when planning, executing, reviewing, or interpreting scientific or ML work intended to support a knowledge claim.
---

# Scientific Work

Scientific automation should produce reliable insight, not merely completed
runs or improved metrics. Harness retains responsibility for the question,
experimental validity, interpretation, and claims even when implementation is
delegated.

## Principles

For a proposed research direction, ask whether it offers contribution,
insight, utility, or novelty, and what evidence would establish that value.
Surface constraints that may invalidate an otherwise attractive result,
including latency, compute or data cost, memory, deployment compatibility,
safety, and whether downstream work requires exact rather than approximate
behavior. Record material constraints in the project spec or exploration note.

## Workflow

1. Define the question and mode: bounded engineering optimization, controlled
   hypothesis test, exploratory evidence gathering, or potential publishable
   claim.
2. Establish why an answer is valuable. Use `scientific-brainstorming` for
   broad direction-finding and `literature-review` to ground state-of-the-art
   or novelty claims.
3. State hypotheses, baselines, controls, metrics, confounders, failure
   conditions, and stopping criteria before decisive experiments.
4. Use `entrypoint` or `research-lookup` for sourced evidence,
   `exploratory-data-analysis` before treating patterns as hypotheses,
   `hypothesis-generation` for competing explanations, `test-hypothesis` for
   controlled comparisons, `statistical-analysis` for quantitative inference,
   and `scientific-critical-thinking` when assessing evidence or conclusions.
5. Validate that implemented experiments match the intended intervention
   before interpreting measurements.
6. Analyze alternatives, negative results, sensitivity, and whether a metric
   change answers the actual question.
7. Separate observed evidence, interpretation, uncertainty, and recommendation
   in the deliverable. Use `write-scientific`, `scientific-visualization`,
   or `scientific-schematics` only when the output needs them.
8. Keep project reports, figures, exports, and agent-produced artifacts under
   `<task-arc-dir>/artifacts/`; use the vault for
   structured knowledge and links to those artifacts.

## Rules

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

## Failure Modes

For nontrivial open-ended work or any consequential claim, actively guard
against the six recurring failure modes reported by Trehan and Chopra from
four autonomous ML-research attempts, three of which failed during
implementation or evaluation:

| Failure Mode | Required Guardrail |
| --- | --- |
| Bias toward training-data defaults | Verify current libraries, datasets, protocols, and stated constraints instead of silently substituting familiar defaults. |
| Implementation drift under execution pressure | Check implementation fidelity before interpreting output; do not accept a simpler running method as the proposed intervention. |
| Memory and context degradation over long tasks | Preserve the agreed specification, configurations, decisions, and accepted results in project files; re-read them before continuation or writing. |
| Overexcitement that declares success despite obvious failures | Inspect raw outputs, failed runs, degeneracies, and baselines before accepting summary narratives or claiming contribution. |
| Insufficient domain intelligence | Identify tacit assumptions and obtain appropriate domain review before selecting consequential baselines or interpreting results. |
| Weak scientific taste in experimental design | Test whether the question matters and the design can answer it; reject trivial, infeasible, underpowered, or statistically invalid experiments. |

Source: Dhruv Trehan and Paras Chopra, [*Why LLMs Aren't Scientists Yet:
Lessons from Four Autonomous Research Attempts*](https://arxiv.org/abs/2601.03315),
arXiv:2601.03315, January 6, 2026.
