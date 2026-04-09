---
name: paperbanana-diagrams
description: Generate high-resolution architectural and methodology diagrams from
  text descriptions using the paperbanana CLI. Provides an automated, iterative visual
  feedback loop to refine diagrams using Gemini 3 and Google Imagen. Use this skill
  when the user asks to "generate a diagram", "visualize the architecture", "draw
  an agent swarm", or "create a paperbanana diagram". Don't use for generic markdown
  generation or when simple Mermaid is sufficient.
---
# PaperBanana Diagrams Skill

This skill explains how to use the `paperbanana` CLI to generate high-quality `.png` architecture and methodology diagrams from text inputs. The CLI runs an iterative visual loop (the "Ralph Wiggum" loop) out-of-the-box, applying a Planner -> Stylist -> Critic workflow to produce publication-ready images.


## Prerequisites

1.  PaperBanana needs text files as its input. If you have an idea for a diagram, write the structure (components, data flows, relationships) into a temporary text file.
    Example: `write_to_file` into `/tmp/diagram_input.txt`.
2.  Be sure to select an appropriate VLM model. `gemini-3-flash-preview` is heavily recommended for the generative loop steps.

## Command Syntax

Use the `paperbanana generate` command.

```bash
paperbanana generate -i <input_text_file> -c "<description_or_caption>" -o <output_png_path> --vlm-model <vlm_model_name>
```

### Example

Generate a diagram of a "Core Agent Pipeline":

1. Write the components to a text file:
```bash
cat << 'EOF' > /tmp/pipeline_input.txt
1. User Input
2. Orchestrator Agent (routes query)
3. SQL Analyst Agent (queries Datahub)
4. Stats Analyst Agent (performs regressions)
5. Critic Agent (evaluates results)
6. Final Output
EOF
```

2. Run the generator:
```bash
paperbanana generate -i /tmp/pipeline_input.txt -c "Core Agent Pipeline with Critic Workflow" -o docs/agent_pipeline.png --vlm-model gemini-3-flash-preview
```

## How It Works (The Iterative Loop)

When you execute the command, `paperbanana` performs the following steps automatically:
1.  **Planner**: Interprets your text input and contextual prompt.
2.  **Stylist**: Enhances and formats the output for the image generator.
3.  **Generator**: Produces the initial image.
4.  **Critic**: Visually evaluates the generated image. If text is garbled, boxes overlap, or lines are missing, the Critic requests a revision.
5.  **Iteration**: Repeats up to a max limit (default usually 3) until the Critic accepts the image.

The CLI will output logs like `[info ] Diagram saved ...` and `[info ] Running critic agent ...` and eventually output the final path (e.g. `docs/agent_pipeline.png`).

### Handling Output Quirks

Often, PaperBanana will output intermediate and final diagrams into a timestamped directory (e.g., `docs/run_20260307_041002/final_output.png`) instead of your exact `--output` target path, and may fail to move it if `--output` is a directory instead of a file.

**Best Practice:**
If your outputs end up inside `run_*` directories, find and move them to their intended destination:

```bash
find docs/run_2026* -name "final_output.png" -exec sh -c 'd="$(dirname "{}")"; bd="$(basename "$d")"; cp "{}" "docs/final_$bd.png"' \;
```
Or manually list the directory and move the image `mv docs/run_20260307_XXXXXX/final_output.png docs/my_diagram.png`.

## Principles

- **Detailed Inputs**: The more specific your text file (`-i`), the better the generated image.
- **Visual Iteration**: Let the tool handle the trial-and-error. You do not need to manually call the Critic agent or loop the CLI yourself; `paperbanana` does this natively.

## Evaluation
For evaluation criteria, see [references/evaluate.md](references/evaluate.md).
