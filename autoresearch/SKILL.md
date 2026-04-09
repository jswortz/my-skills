---
name: autoresearch
description: Autonomous research loop inspired by karpathy/autoresearch. Iteratively modify a target file (config, prompt, code), run an experiment with a fixed evaluation metric, keep improvements, discard regressions, and log everything to a TSV. Use when optimizing prompts, tuning hyperparameters, evolving agent configurations, or running overnight autonomous improvement loops.
---

# Autoresearch Skill

Autonomous experiment loop for iterative research. Inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch): modify code, run experiment, measure metric, keep or discard, repeat.

## Core Pattern

```
LOOP:
  1. Hypothesize — form an idea based on past results
  2. Modify — edit the target file(s)
  3. Commit — snapshot the change
  4. Run — execute the experiment (fixed budget)
  5. Measure — extract the key metric
  6. Decide — keep (metric improved) or revert (metric worse/equal)
  7. Log — record result in results.tsv
  GOTO 1
```


## Advanced Details & Examples
For advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).
