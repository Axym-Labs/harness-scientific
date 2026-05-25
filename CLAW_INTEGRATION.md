# Claw Curated Integration

This fork is based on
[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills),
an MIT-licensed and widely used scientific skill collection. Claw loads only
the skills under `claw-skills/`, not the entire upstream `scientific-skills/`
catalog.

## Rationale

The upstream repository is a useful high-quality starting point, particularly
its `scientific-critical-thinking`, `literature-review`, and
`hypothesis-generation` workflows. It is also broad and contains assumptions
that should not silently become Claw defaults, including tool/API dependencies
and mandatory generated-figure instructions.

The curated layer:

- adapts the upstream rigor and literature-review methods for this installation;
- adds the local controlled-experiment and durable-research workflows;
- incorporates failure modes from Yuxi Liu's critique of fully autonomous
  research agents; and
- keeps scientific judgment, verification, and claims under Claw/user review.

## Loaded Skills

| Skill | Origin and adaptation |
|-------|-----------------------|
| `scientific-critical-thinking` | Concise adaptation of the upstream skill, with experimental validity and ML claim checks; mandatory visual-generation instructions omitted. |
| `literature-review` | Concise adaptation of the upstream skill, independent of optional search backends. |
| `scientific-work` | Integration protocol for scientific planning, execution, and interpretation. |
| `research` | Local durable evidence-collection workflow moved from the Claw core. |
| `test-hypothesis` | Local controlled-experiment workflow moved from the Claw core and strengthened for claim validity. |

Reference:

- Yuxi Liu, ["Who is Seriously Using Claw Scientist to do Fully Autonomous Research? Please Don't"](https://www.linkedin.com/pulse/who-seriously-using-claw-scientist-do-fully-autonomous-liu-hlmrc/)
