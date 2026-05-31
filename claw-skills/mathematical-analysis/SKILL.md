---
name: mathematical-analysis
description: Use when analyzing mathematical objects, formalizing mathematical problems, or deriving nontrivial mathematical claims where precision, representation choice, and sourced unfamiliar steps matter.
---

# Mathematical Analysis

## Principles

- Explicitly specify and delimit the mathematical objects under consideration:
  sets, spaces, functions, operators, graphs, measures, objectives,
  equivalence relations, assumptions, and boundary cases.
- For non-well-known mathematical knowledge or non-obvious derivation steps,
  provide sources or say what must be verified.
- Prefer exact statements over qualitative descriptions. Mark conjectures,
  heuristics, analogies, and proven claims differently.

## Useful Primitives

- Gather representations of the problem and state what a solution would look
  like in each representation.
- Translate the problem into its platonic information when applicable: the
  representation where most problems about that mathematical object become
  simplest to state or solve.
- View symbolic manipulation as a graph when useful. Simple operations form
  local clusters; progress often requires nontrivial translations between
  clusters.
- Track invariants, symmetries, conserved quantities, duals, normal forms,
  decompositions, limits, and counterexamples.
- Check whether a known theorem actually solves the posed problem or merely
  resembles it.

## Failure Modes

- **Imprecision and hand-waving**: undefined objects, implicit assumptions, or
  skipped equivalence steps.
- **Purely phenomenological analysis**: qualitative story without formal
  objects, transformations, or checks.
- **Unhelpful collapse to known results**: naming a true theorem or standard
  framing that does not answer the strict problem.
