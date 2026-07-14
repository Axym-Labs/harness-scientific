# Harness Curated Integration

This fork is based on
[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills),
an MIT-licensed and widely used scientific skill collection. Harness loads only
the skills under `harness-skills/`, not the entire upstream `scientific-skills/`
catalog.

## Rationale

The upstream repository is a useful high-quality starting point, particularly
its `scientific-critical-thinking`, `literature-review`, and
`hypothesis-generation` workflows. It is also broad and contains assumptions
that should not silently become Harness defaults, including tool/API dependencies
and mandatory generated-figure instructions.

The curated layer:

- adapts the upstream rigor and literature-review methods for this installation;
- adds the local controlled-experiment and durable-research workflows;
- incorporates failure modes from Yuxi Liu's critique of fully autonomous
  research agents; and
- keeps scientific judgment, verification, and claims under Harness/user review.

## Loaded Skills

| Skill | Origin and adaptation |
|-------|-----------------------|
| `scientific-critical-thinking` | Concise adaptation of the upstream skill, with experimental validity and ML claim checks; mandatory visual-generation instructions omitted. |
| `literature-review` | Concise adaptation of the upstream skill, independent of optional search backends. |
| `hypothesis-generation` | Competing hypotheses and discriminating experiments, without mandatory generated assets. |
| `peer-review` | Formal manuscript/grant review with additional computational/ML checks. |
| `research-lookup` | Source retrieval routed through tools available in the current environment. |
| `scientific-schematics` and `scientific-visualization` | Optional, scientifically honest visual communication. |
| `scientific-brainstorming` | Structured exploration that must transition into evidence gathering or testing. |
| `statistical-analysis` and `exploratory-data-analysis` | Quantitative analysis and data-quality workflows without assumed optional packages. |
| `scientific-work` | Integration protocol for scientific planning, execution, and interpretation. |
| `research` | Local durable evidence-collection workflow moved from the Harness core. |
| `test-hypothesis` | Local controlled-experiment workflow moved from the Harness core and strengthened for claim validity. |
| `arxiv` | arXiv PDF/source download and metadata search skill created by Tim Scarfe, packaged with its bundled CLI for local use. |

Scientific writing now lives in the owned writing suite as `write-scientific`.

Reference:

- Yuxi Liu, ["Who is Seriously Using Harness Scientist to do Fully Autonomous Research? Please Don't"](https://www.linkedin.com/pulse/who-seriously-using-harness-scientist-do-fully-autonomous-liu-hlmrc/)
