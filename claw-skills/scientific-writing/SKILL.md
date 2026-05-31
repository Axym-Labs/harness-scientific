---
name: scientific-writing
description: Use when drafting or revising scientific manuscripts, abstracts, methods, results, discussions, or research reports.
---

# Scientific Writing

Adapted from K-Dense's upstream `scientific-writing` skill. Accuracy,
traceability, and clarity take priority over ornamental completeness. For ML
papers, this incorporates Jakob Foerster's *How to ML Paper - A Brief Guide*.

## Workflow

1. Establish document type, intended audience or venue, evidence available,
   reporting standard if applicable, and citation style.
2. Select a paper form and its evidentiary burden before drafting:

   | Form | Central burden |
   |------|----------------|
   | Empirical method/system | Fair comparisons, ablations, robustness, reproducibility |
   | Theoretical/analytical | Precise claims, assumptions, proofs or derivations, implications |
   | Dataset/benchmark/evaluation | Provenance, intended uses, validity, biases, supported claims |
   | Survey/position/conceptual | Defensible scope, faithful synthesis or argument, limitations |

3. Ground factual and novelty claims through `entrypoint` or
   `literature-review`; do not invent citations or fill missing evidence with
   confident prose.
4. Outline each section around one necessary function and draft the abstract
   early enough to expose an unclear contribution or missing experiment.
5. Keep observations/results separate from interpretation. State effect sizes,
   uncertainty, controls, limitations, negative results, and relevant
   reporting requirements.
6. Use `scientific-critical-thinking` before finalizing consequential claims.
7. Store project manuscripts and rendered/exported outputs under
   `<project-dir>/docs/<task-arc>/artifacts/`.

## Principles

Use the venue's format when specified. For a typical ML research paper:

| Section | Job |
|---------|-----|
| Abstract | State the problem and relevance, why it is hard, the contribution, and the evidence that supports it. |
| Introduction | Expand that argument and state distinct contributions explicitly. |
| Related work | Identify close alternatives, compare assumptions and methods, and explain or run applicable comparisons. |
| Background / problem setting | Give the concepts, notation, assumptions, and task needed to understand the contribution; separate a novel problem setting when it is itself a contribution. |
| Method | Explain what is proposed and why it should work, with adequate formal detail. |
| Experimental setup | Specify datasets, baselines, tuning protocol, implementation, compute, metrics, and statistical procedure. |
| Results and discussion | Match evidence to claims: fair baselines, uncertainty, ablations, robustness, failures, and limitations. |
| Conclusion | Recap supported contributions and bounded future work. |

Not every paper is an empirical method paper: adapt this shape to the selected
paper form rather than pretending a position, theory, or dataset contribution
is an algorithm leaderboard paper.

## Failure Modes

- Blurring prior work, a problem definition, and the paper's own
  contributions. State exactly what is new.
- Claiming superiority without applicable baselines, fair tuning, uncertainty,
  ablations, or the assumptions under which the comparison holds.
- Treating setup details, limitations, negative results, data/code
  availability, or compute requirements as optional when they affect the
  claim or reproducibility.
- Making broad or grandiose claims without sources or experimental support.
- Introducing notation, acronyms, or work-specific terminology late, then
  varying that terminology with synonyms.
- Hiding the actor or contribution through needless passive voice, filler
  (`can`, `in order to`, `shall`), vague adjectives, or inconsistent tense.
- Duplicating tables/figures in prose, leaving broken references, or including
  a symbol that is never used.

## Rules

- Write finished manuscript text as coherent prose unless the requested genre
  calls for a checklist or table.
- Include figures or schematics only when they clarify methods, results, or
  mechanisms; they are not mandatory by default.
- Every citation must correspond to a checked source, and every broad claim
  should be proportionate to the evidence.

## Sources

- Upstream base: K-Dense `scientific-writing`, retained selectively because
  mandatory generated-figure requirements are not generally valid.
- ML guidance: Jakob N. Foerster, *How to ML Paper - A Brief Guide*,
  <https://www.jakobfoerster.com/how-to-ml-paper>.
