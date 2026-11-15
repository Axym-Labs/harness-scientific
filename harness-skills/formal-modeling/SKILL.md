---
name: formal-modeling
description: Use when turning an intuition, free-text description, or informal research question into a formal model or framework, or when choosing between candidate formalizations of a problem.
---

# Formal Modeling

## Principles

- Choose the simplest model that still expresses the question. Start with the
  fewest objects, variables, and parameters, and add structure only when the
  simpler model demonstrably cannot state what is asked.
- Model the question directly, not a more general class of problems. Prefer
  a concrete instance (finite, linear, scalar, two-component) before the
  general case.
- Every element must earn its place: tie each object, variable, and
  assumption to a feature of the intuition, and delete the rest.
- Reuse a standard framework when it fits exactly (dynamical system,
  optimization problem, Markov chain, game, graphical model). Do not invent
  notation for a known object, and do not force a known framework onto a
  question it does not answer.

## From Intuition To Model

1. State the intuition in one or two plain sentences. Its nouns are candidate
   objects, its verbs candidate maps or dynamics, and its assertion the
   candidate claim.
2. Map each to a formal object. Say what is observed or latent, fixed or
   varying, and on which timescale.
3. Write the claim as a precise statement inside the model (equation,
   inequality, limit, or existence statement) that could turn out false.
4. Translate back: read the model in plain words and check that it says what
   the intuition says, with nothing lost and nothing added. List what the
   model deliberately omits.
5. Check a toy instance or limiting case where the answer is known.

## Failure Modes

- **Framework inflation**: general machinery or notation that the question
  never uses.
- **Proxy model**: a tractable model of a different question.
- **Smuggled assumptions**: structure introduced during formalization that the
  intuition did not contain, left unstated.

Once the model is fixed, use `mathematical-analysis` for precise statements,
derivations, and proofs within it.
