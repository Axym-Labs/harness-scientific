---
name: research-taste
description: Research judgment, selection, and quality. Use broadly when evaluating research directions, choosing which ideas deserve work, or judging rigor and contribution quality.
---
# Research Taste: Judgement, Selection, and Quality

## Core Insights

1. Feynman: self-deception is the first enemy  
   Use the rule: "you must not fool yourself."  
   Before trusting a result, ask what you may have hidden from yourself: bad controls, cherry-picked examples, confounded evaluation, or a story invented after seeing the answer.

2. Platt: prefer disproof-shaped experiments  
   Good experiments are organized around "alternative hypotheses" and a "crucial experiment."  
   A result has better taste when it rules out nearby explanations, not merely when it supports your favored one.

3. Domingos: generalization is the actual target  
   In ML, "generalization" matters more than training performance or benchmark theater.  
   Watch for leakage, repeated validation-set tuning, weak baselines, and distribution shifts hidden behind aggregate metrics.

4. Domingos: separate representation, evaluation, optimization  
   Use the decomposition "representation + evaluation + optimization."  
   When judging a paper, ask which part actually improved; many papers claim a new algorithm when the real gain is representation, data, metric choice, or tuning.

5. Domingos: overfitting is not only a train/test curve  
   "Overfitting has many faces."  
   A research community can overfit too: to benchmarks, reviewer preferences, fashionable narratives, or a narrow set of tasks.

6. Peyton Jones: writing is a test of thought  
   Use "Don't wait: write."  
   Draft the abstract, contribution, and strongest objection early; unclear writing often reveals unclear research.

7. Shannon: simplify to the essentials  
   Shannon recommends "simplification": cut the problem down until only the essential difficulty remains.  
   A tasteful contribution often looks smaller than the original ambition but sharper, more inspectable, and more reusable.

8. Feynman: keep the full evidence visible  
   Scientific integrity requires showing the evidence that could make you look wrong.  
   A paper that only presents supporting evidence is not necessarily false, but it is not yet trustworthy.

## Project Selection and Strategy (ML, 2026 Evidence)

Defaults for choosing and shaping projects, from a study of how ML papers and
researchers succeed (forums, insider accounts, ICLR 2023-2026 data; report in
`~/main/harness/infra-internal/paper-writing-practice/artifacts/final/`).

- **Pilot fast, commit late.** Pilot an idea for days and drop it if the
  pilot fails; work in project cycles of one to two months, with a
  submit-or-stop date. There is no time for long upfront commitments to an
  untested idea. Keep a coherent topic over years: far pivots are penalized
  (lowest-pivot work reaches the top 5% of citations 7.4% of the time, highest
  pivot 2.2%), and staying near one's topic helps a little.
- **Frame toward strong areas when the work allows it.** LLM-adjacent framing
  goes with 0.2-0.3 SD higher review scores and about 3-4 times the
  citations; relabelling toward LLM applications or other favoured areas is
  valid, widely used, and likely to move the bar. Encourage it whenever the
  opportunity is significant for the work, which it often is.
- **Target mechanism and benchmark together.** A SOTA record lasts a median of
  about ten months and accepted papers are presented five to six months after
  arXiv, so mechanisms, framings, and failure analyses outlive rank claims;
  aim for both rather than choosing.
- **Scale the claim to the compute.** Check before running that the
  available scale can show the effect; if not, choose a claim small scale
  settles (a mechanism, a controlled failure case, a theorem). A marginal
  small-scale test of a good idea reads as evidence against it: Transformers
  for vision were tried and dropped before ViT won with about 100M images.
- **Being first within months barely matters.** In concurrent pairs, the
  earlier paper won 17 of 28 (famous pairs) and 12 of 22 (random sample);
  the winner still collects 2-3.5 times the runner-up's citations. What goes
  with winning: general framing, breadth of demonstration, a reusable
  artifact, and early attention.
- **Review scores barely predict citations within a tier** (Spearman 0.17
  within ICLR posters, about 0 within orals); acceptance and impact are
  different targets.
- **Make artifacts adoptable, not just available.** A public repository
  linked from arXiv; for baselines, integration into an existing library
  (Mammoth, Avalanche for continual learning). Code goes with 1.4-1.7 times
  the citations (an upper bound); where tooling is nearly empty (local
  learning rules), a benchmark or library is a low-competition bet.
- **Venues: prefer A and A+ conferences on coherent research topics**, as for
  a cumulative PhD thesis. Views on TMLR's standing split ("no serious ML
  researcher would value TMLR over NeurIPS/ICML/ICLR" against "about the same
  as a non-oral top-tier paper"). Advice on the first venue splits too ("aim
  high and you get the middle" against practising at a tier-2 venue first);
  it depends on whether a senior reader is available.
- **One credible co-author per paper**, for verification, letters, arXiv
  endorsement, and distribution. At ICLR 2023-2026, solo papers score 0.67 SD
  below 3-4-author papers and student-only teams 0.50 SD below teams with any
  non-student, while professor-led teams score no higher than postdoc-led
  ones; nearly all of these gaps are in the reviewer scores. Senior
  co-authorship early goes with more citations, most at weaker institutions,
  while topic independence from the mentor later helps. Network position
  matters less than it looks: author centrality is the strongest bivariate
  citation predictor but adds about 0.003 explained variance once content is
  controlled. Cheap paths: ML
  Reproducibility Challenge reproductions, library integration, challenges,
  MATS-type programs, short targeted messages to first authors.
- **Environment and advisor attention** are named on every Chinese platform
  as outweighing craft ("individual effort can hardly exceed the effect of
  the platform"); untested, but consistent with the co-author data.
- **Plan around quotas and endorsement:** each paper needs an author who
  qualifies as a reciprocal reviewer (otherwise one paper per author at ICLR
  and ICML 2027); TMLR allows 2 solo papers a year; arXiv allows 2
  submissions a month; arrange endorsement through a co-author early.
- **Build the record each gatekeeper reads:** first-author main-track papers
  for research-scientist roles; work samples and public write-ups for labs
  and fellowships (Anthropic asks for independent research and open source at
  the top of the resume); letters from people the committee knows for PhD
  programs; few middle authorships; workshop papers labelled as such;
  application answers written yourself. Offers come mostly through people
  who know the work: for each paper, name whom it should reach, and present
  it in person (a cancelled conference cost scheduled papers 5 points in the
  chance of being cited within four years, more for early-career authors).
- **Agents: keep the decisions, verify from artifacts.** Fix the claim,
  acceptance criteria, and a written prediction before a run; check data
  provenance, full test-set size, and that selection used only train or
  validation data; recompute numbers from logs; treat "done" or "not
  possible" as no evidence; make honest failure the cheapest exit ("if X is
  impossible, stop and report; never substitute data"), which cut undisclosed
  fabrication from 20.6% to 3.2% in one benchmark. Use scripts to check
  numbers and LLM critics to look for alternative explanations. AI help
  raises output but does not build the skill unless one works to understand
  the output; write the first draft of the core argument yourself.
- **Confidentiality:** API or commercial tiers, or the training toggle off;
  no feedback buttons or share links in sessions with an unpublished core
  idea; a timestamped private git record; when a result is announced, post
  the paper rather than teasing it.

## Olah Research Taste Exercises

- List research ideas and ask a respected mentor to rate them; study cases
  where you disagree after reflection.
- When someone publishes an idea you had, compare the result to your
  expectations and update your taste.
- Interview researchers about why they work on their problems, how they pick
  them, and what larger research picture they are pursuing.
- Critique your own community's taste: where might it be wrong, and what do
  adjacent research schools see differently?
- Ask the anti-Hamming question: what are the most interesting problems in the
  field, and why are you not working on them?
- Before spending a month or more, write a short project proposal explaining
  why the question matters, why the answer would be valuable, what you expect,
  and what early evidence supports that expectation.
- Imagine another group published the paper you are considering; would you be
  excited to read it?

## What is Research?

Research is anything but homework. Finding a good problem to study is part of research. Research is about pushing the limits: dismiss the problem if the solution is not interesting. Research is a game for which you get to set the rules, but it cannot be a trivial one!

What is the difference between a homework problem and a research problem? Probably no [difference], except for your [ownership of it].

## What is Engineering Research?

Engineering is about optimization, but engineering research is not! Research is to find the limits and better ways for [optimization].

Engineering is about invention, but engineering research is not! Research is to explain why an invention [works].

Engineering research is neither science nor empirical science. It is more like applied mathematics and applied [theory].

A good engineer needs not to be a good researcher; a good researcher needs not to be a good [engineer].

Research is all about generalizability, whereas engineering is about instantiation and [application].

## What is Good Research?

A good research result has:
- **Novelty** (better if you were not able to publish it at first)
- **Simplicity** (better if your advisor refused to grant you a degree)
- **Universality** (better if others found it trivial at first sight)

You recognize a great research result if it keeps you up all night, feeling like your first [love].

## How to Develop Good Taste

Engineering science is neither science nor empirical science! It is more like applied mathematics and applied [physics].

Research is all about generalizability, whereas engineering is about instantiation and [specialization].

## Warning Signs of Bogus Research

1. Prove by successful instances  
   Showing many cases where a method works is not the same as proving that the underlying problem has been solved. Successful examples can be useful evidence, but they do not explain why the method works, when it fails, or whether it reduces the real difficulty of the problem.

2. Compound and conquer  
   This means gluing many partial solutions into a large system and claiming progress because the whole pipeline works on some tasks. The danger is that the assumptions of the parts may not be compatible, and the resulting system may be too complex to analyze clearly.

3. Results too complicated to reproduce  
   If a result depends on too much code, hidden data, undocumented tuning, or unavailable infrastructure, others cannot independently verify it. In science, a result that cannot be reproduced remains weak no matter how impressive it looks.

4. Reinvent the wheel without proper acknowledgment  
   A researcher may rediscover an old idea, rename it, and present it as novel. Reusing old ideas is fine, but the contribution must be honestly positioned relative to prior work.

5. Tackle ill-posed problems directly  
   Real-world problems are often messy, with conflicting goals and unclear definitions. Good research usually extracts a precise subproblem first; bogus research often attacks the vague full problem directly and hides the lack of rigor behind empirical success.

6. Solicit popularity over expert opinions  
   Citations, demos, publicity, or broad appeal can make work look important even when experts see little depth. Popularity may reflect accessibility or hype rather than originality, correctness, or long-term scientific value.

7. Occam's razor reversed  
   Instead of preferring the simplest adequate explanation or model, the researcher keeps adding parameters, modules, and heuristics until the results look good. This can turn evaluation data into part of the tuning process and make the claimed insight meaningless.

## Protect Your Reputation and Scholarship

**Green zone (Good practice):**
- Adequate references
- Protect copyright
- Retract false results
- Share ideas & credits
- Fair competition

**Gray zone (Questionable practice):**
- Selective reference
- Double submission
- Cherry-pick results
- Borrow ideas steal credits
- Unfair comparison

**Red zone (Unacceptable):**
- Plagiarism
- Self plagiarism
- Fabricating results
- Steal ideas
- Sabotage others

The only person you could cheat is yourself!

## The Right Attitudes

Be both confident and humble (about your own work)
Be both critical and appreciative (about other's work)
Be both ambitious and realistic (about your research plan)
Be both aggressive and generous (about credits)

Be proactive and willing to take a chance!
The only way you can improve yourself is to learn things that you are the most afraid of!

## Prepare Yourself Psychologically

1. Is being a top student enough? Neither necessary nor sufficient...
2. Do you know your intellectual or mental limit? Ready for failures?
3. Are you extremely motivated? All you need is passion...

Research is not a job, and is more like a hobby!

## How Does Doing Research Feel Like?

1. An endless cycle between excitement and depression...
2. An endless cycle between sense of success and failure...
3. An endless cycle between over-confidence and self-doubt...

Research needs faith in there are always interesting new things for you to discover and by doing so you can make the world a better place!

## Mentality: The Right Attitudes

Be both confident and humble (about your own work)
Be both critical and appreciative (about other's work)
Be both ambitious and realistic (about your research plan)
Be both aggressive and generous (about credits)
