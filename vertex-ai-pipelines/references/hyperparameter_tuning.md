# Hyperparameter Tuning with GCPC

Vertex AI provides managed hyperparameter tuning accessible directly via `google_cloud_pipeline_components`.

## Key Concepts

1.  **Define worker pool specs**: This dictates the machine types and base containers inside which tuning takes place.
2.  **Define metrics**: Specify the objective (e.g., maximize accuracy).
3.  **Define parameters**: Provide search space (e.g., learning rate between 0.001 and 0.1).
4.  **Extract best trial**: After the study finishes, parse the output of the tuning job to grab the best trial's metrics or artifacts.

### Example Pipeline Component

```python
from google_cloud_pipeline_components.v1.hyperparameter_tuning_job import HyperparameterTuningJobRunOp

@component(packages_to_install=['google-cloud-aiplatform', 'google-cloud-pipeline-components', 'protobuf'], base_image='python:3.7')
def get_best_trial_op(gcp_resources: str, study_spec_metrics: list) -> str:
    # Logic to parse the Tuning job GCP resources and return the best trial parameters
    pass

@dsl.pipeline(name="hp-tuning-pipeline")
def my_tuning_pipeline():
    tuning_op = HyperparameterTuningJobRunOp(
        display_name="my-hpt-job",
        project="my-project",
        location="us-central1",
        worker_pool_specs=[{"machine_spec": {"machine_type": "n1-standard-4"}, "replica_count": 1, "container_spec": {"image_uri": "my-training-image"}}],
        study_spec_metrics=[{"metric_id": "accuracy", "goal": "MAXIMIZE"}],
        study_spec_parameters=[{"parameter_id": "learning_rate", "double_value_spec": {"min_value": 0.001, "max_value": 0.1}}],
        max_trial_count=10,
        parallel_trial_count=3,
        base_output_directory="gs://my-bucket/hpt-output",
    )

    trials_op = get_best_trial_op(
        gcp_resources=tuning_op.outputs["gcp_resources"],
        study_spec_metrics=tuning_op.inputs["study_spec_metrics"]
    )
```
