## Setup

Before starting the loop, establish:

1. **Target file(s)**: What gets modified each iteration (e.g., `train.py`, `prompt.md`, `config.yaml`, `swarm_manager.py`)
2. **Run command**: How to execute the experiment (e.g., `uv run train.py`, `novastorm deploy --epochs 5`)
3. **Metric**: What to optimize (e.g., `val_bpb` lower-is-better, `avg_score` higher-is-better, `bootstrapping_rate` higher-is-better)
4. **Extraction command**: How to get the metric from output (e.g., `grep "^val_bpb:" run.log`)
5. **Time budget**: Max time per experiment (e.g., 5 minutes, 1 hour)
6. **Branch**: Create `autoresearch/<tag>` branch for the run
7. **Baseline**: Run unmodified code first to establish starting metric

### Initialize Results Log

Create `results.tsv` with header:

```
commit	metric	status	description
```

## The Experiment Loop

### Step 1: Hypothesize

Review past results in `results.tsv`. Consider:
- What worked? Try variations of successful changes
- What failed? Avoid similar approaches
- What's unexplored? Try orthogonal ideas
- Can successful changes be combined?

### Step 2: Modify Target File

Make ONE focused change per experiment. Examples:
- **Prompt tuning**: Adjust instructions, add constraints, change examples
- **Hyperparameters**: Learning rate, batch size, temperature, thresholds
- **Architecture**: Model config, tool selection, agent structure
- **GEPA tuning**: Mutation rate, elite retention, crossover probability, fitness scaling

### Step 3: Commit

```bash
git add <target-file>
git commit -m "experiment: <brief description>"
```

### Step 4: Run

```bash
<run-command> > run.log 2>&1
```

Redirect all output — do NOT flood context. If using a long-running pipeline, use background execution and poll for completion.

### Step 5: Measure

```bash
<extraction-command>
```

If empty output → experiment crashed. Run `tail -n 50 run.log` to diagnose.

### Step 6: Decide

- **Metric improved** → KEEP. Advance the branch.
- **Metric equal or worse** → DISCARD. `git reset --hard HEAD~1`
- **Crashed** → Attempt quick fix (typo, import). If fundamentally broken, discard and move on.

**Simplicity criterion** (from Karpathy): A tiny improvement that adds ugly complexity is not worth it. Removing something and getting equal or better results is a great outcome.

### Step 7: Log

Append to `results.tsv`:

```
<commit>	<metric>	<keep|discard|crash>	<description>
```

### Repeat

NEVER STOP unless manually interrupted. If out of ideas:
- Re-read target files for new angles
- Try combining previous near-misses
- Try more radical changes
- Review the literature or docs

## Applying to NovaStorm

### Optimizing GEPA Parameters

```
Target: src/swarm_manager.py (or .env)
Run: novastorm deploy --epochs 5 --concurrency 10
Metric: bootstrapping_rate (higher is better), avg_score (higher is better)
Extract: Parse progress.json from GCS after pipeline completes
Budget: ~30 minutes per experiment
```

Variables to tune:
- `RANDOM_MUTATION_RATE` (currently 0.25)
- `ELITE_RETENTION_RATE` (currently 0.2)
- `FITNESS_SCALING_FACTOR` (currently 0.08)
- `CROSSOVER_RATE` (currently 0.25)
- `ADAPTIVE_THRESHOLD_FLOOR` (currently 0.25)
- `DIVERSITY_SCALING` (currently 0.4)

### Optimizing Skill Synthesis Prompts

```
Target: src/swarm_manager.py (skill_architect prompt)
Run: novastorm deploy --epochs 5 --concurrency 10
Metric: tool_diversity (% of insights using 3+ distinct tools), bootstrapping_rate
Extract: Parse JSONL logs from GCS
Budget: ~30 minutes per experiment
```

### Optimizing Critic Scoring

```
Target: src/critic_agent.py
Run: novastorm deploy --epochs 5 --concurrency 10
Metric: score_variance (lower variance = more consistent), threshold_convergence
Extract: Parse JSONL logs for score distribution
Budget: ~30 minutes per experiment
```

### Fast Local Experiments (No Pipeline)

For quick iterations without deploying a full pipeline:

```
Target: src/swarm_manager.py
Run: uv run pytest tests/test_swarm_manager.py -v
Metric: test pass rate, phase diversity in test output
Extract: pytest exit code + grep test output
Budget: ~30 seconds per experiment
```

## Results TSV Format

Tab-separated. Do NOT use commas in descriptions.

```
commit	metric	status	description
a1b2c3d	0.380	keep	baseline: 5 epochs default params
b2c3d4e	0.420	keep	increase MUTATION_RATE from 0.25 to 0.35
c3d4e5f	0.390	discard	decrease ELITE_RETENTION to 0.05
d4e5f6g	0.000	crash	set CROSSOVER_RATE to 1.0 (division by zero)
e5f6g7h	0.570	keep	combined: MUTATION=0.35 + SCALING=0.06
```

## Key Principles

1. **One change at a time** — isolate variables so you know what caused improvement
2. **Fixed evaluation** — same epochs, concurrency, and dataset across experiments
3. **Keep or discard** — no partial keeps. Binary decision per experiment
4. **Log everything** — even crashes are data points
5. **Simplicity wins** — if removing code gives equal results, that's a win
6. **Autonomous** — don't stop to ask. Run until interrupted
7. **Compound gains** — small improvements stack. 1% per iteration × 100 iterations = transformative
