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
- The bundled paper-like Matplotlib style is `assets/paper.mplstyle`; resolve
  it from the directory containing this `SKILL.md` when useful.
- If a core performance figure compares our methods with baselines, use
  `#3F21B6` for the primary method, the lighter same-hue `#8C7AD3` for a
  secondary method, and the darker neutral `#7A7A7A` for every baseline or
  comparison. Keep the primary method visually dominant; do not give a
  comparison another accent color.
- Use a table for simple data. For richer data, prefer line plots, more complex
  plots, and information-dense views such as a metric over a two-dimensional
  plane.
- When a scatterplot represents a relationship that can be estimated
  responsibly, try a smooth fitted curve while retaining the observations and
  avoiding fabricated structure.
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
5. Store figure files under `<task-arc-dir>/artifacts/`.
6. Use `scientific-critical-thinking` when a plot supports a substantive
   claim, and `scientific-schematics` for conceptual rather than measured
   content.
7. Do not use lollipop plots or heatmaps. If the information is simple enough
   for a heatmap, prefer a table when it is worth displaying at all.
8. Omit plot titles unless the figure is surely internal; put the necessary
   context in the surrounding document or caption. Capitalize labels.
