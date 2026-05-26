---
name: scientific-visualization
description: Use when selecting, creating, or reviewing plots and visual encodings for scientific or experimental data.
---

# Scientific Visualization

Adapted from K-Dense's upstream `scientific-visualization` skill for honest
data communication.

## Workflow

1. Identify the question the visualization should answer, data type, units,
   uncertainty, grouping, and intended audience.
2. Select a representation faithful to the data: show distributions or raw
   points where informative, include uncertainty definitions, and avoid
   misleading aggregation, axes, or color scales.
3. Use available project plotting libraries and preserve the source code or
   notebook that produced durable figures; store project figure outputs under
   `<project-dir>/docs/artifacts/`.
4. Label axes/units, legends, sample counts, interval/error meanings, and
   preprocessing or exclusions needed for interpretation.
5. Review for accessibility, reproducibility, and whether visual emphasis
   overstates the conclusion.

Use `scientific-critical-thinking` when a plot supports a substantive claim,
and `scientific-schematics` for conceptual rather than measured content.
