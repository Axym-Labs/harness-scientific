---
name: scientific-visualization
description: Use when creating, polishing, or reviewing plots and visual encodings for scientific, experimental, metric, or result data.
---

# Scientific Visualization

## Principles

- Make the plot answer one question; choose axes, aggregation, and annotations
  around that question.
- Prefer paper-like figures: small serif text, restrained styling, high
  contrast, and no decorative effects.
- Use small readable type, usually 7-9 pt at final size; use a serif font when
  available.
- Use vector output (`.pdf` or `.svg`) for durable figures and a `.png` preview
  when useful.
- Preserve the code or notebook that generated the plot next to the artifact.
- Inspect the rendered figure before accepting it: labels, legend, cropping,
  text size, colors, and whether the visual emphasis matches the evidence.

## Rules

1. Label axes with units and define error bars, intervals, preprocessing, and
   sample counts when they matter.
2. Prefer colorblind-safe palettes such as Okabe-Ito; avoid rainbow scales.
3. Do not rely on color alone: use line style, markers, ordering, direct labels,
   or facets when helpful.
4. Use consistent scales for comparisons unless a deliberate exception is
   labeled clearly.
5. Store figure files under `docs/<task-arc>/artifacts/`.
6. Use `scientific-critical-thinking` when a plot supports a substantive
   claim, and `scientific-schematics` for conceptual rather than measured
   content.
