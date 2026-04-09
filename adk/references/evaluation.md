# ADK Agent Evaluation Guide

Evaluating your ADK agents is a critical best practice to ensure predictable and high-quality behavior, particularly when dealing with complex tool usage or multi-agent orchestrations.

## Why Evaluate?
As outlined in recent best practices for skill and agent creation, evaluations provide a deterministic way to validate that your agent responds correctly to various scenarios without regressions over time.

## Running Evaluations against Deployed Agents

You can run evaluations using the Vertex AI `genai.Client().evals` API against deployed ADK agents.

### Evaluation Script
A complete, runnable evaluation script is located at `scripts/run_adk_eval.py`.

### Key Metrics
When evaluating ADK agents, prioritize these metrics:
- `rubric_based_final_response_quality_v1`: Assesses the overall quality of the agent's final response against your specific instructions.
- `tool_use_quality_v1`: Crucial for ADK agents, this metric verifies that the agent is selecting the correct tools and passing the appropriate arguments.

### Process
1. Define `EvalCase` instances with specific `ConversationScenario` setups.
2. Use `client.evals.run_inference` to collect the agent's responses.
3. Use `client.evals.evaluate` to score the responses using Vertex AI evaluators.