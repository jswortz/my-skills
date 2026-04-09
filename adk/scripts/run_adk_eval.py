import os
from google import genai
from google.genai import types

def run_eval():
    PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
    LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")
    AGENT_RESOURCE = os.environ.get("AGENT_RESOURCE")

    if not all([PROJECT_ID, LOCATION, AGENT_RESOURCE]):
        print("Set GOOGLE_CLOUD_PROJECT, GOOGLE_CLOUD_LOCATION, and AGENT_RESOURCE env vars")
        return

    client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)

    eval_cases = [
        types.EvalCase(
            eval_case_id="test_1",
            conversation_scenario=types.ConversationScenario(
                starting_prompt="Run a simulation of 3 shoppers",
                conversation_plan="Ask about endcap conversion rates",
            ),
        ),
    ]

    eval_set = types.EvalSet(eval_set_id="my_eval", eval_cases=eval_cases)

    print("Running inference...")
    result = client.evals.run_inference(
        agent=AGENT_RESOURCE, 
        eval_set=eval_set,
        config=types.RunInferenceConfig(eval_run_id="run_1")
    )

    print("Evaluating...")
    evaluation = client.evals.evaluate(
        eval_set=result,
        metrics=[
            types.EvalMetric(metric_name="rubric_based_final_response_quality_v1"),
            types.EvalMetric(metric_name="tool_use_quality_v1"),
        ],
        config=types.EvaluateConfig(eval_run_id="run_1"),
    )
    print(f"Evaluation complete: {evaluation}")

if __name__ == "__main__":
    run_eval()
