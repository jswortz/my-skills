---
name: vertex-ai-pipelines
description: >
    Develop, construct, and orchestrate Vertex AI Pipelines using kfp and google-cloud-pipeline-components.
    Use when building production ML workflows, deploying custom prediction routines (CPR), writing hyperparameter tuning pipeline components, and ensuring inputs/outputs are tracked with ML Metadata. Don't use for generic Python script execution without Vertex integration.
---

# Vertex AI Pipelines

This skill contains the canonical patterns for developing Vertex AI Pipelines using the current `kfp.v2` (or simply `kfp.dsl`) SDK alongside `google_cloud_pipeline_components`.

## Core Libraries

Always use the following imports when dealing with Vertex AI Pipeline components:

```python
import kfp
from kfp import compiler, dsl
from kfp.dsl import component, Input, Output, Artifact, Dataset, Model, Metrics

# Google Cloud Pipeline Components (GCPC)
from google_cloud_pipeline_components.v1 import dataset, custom_job
from google_cloud_pipeline_components.v1.model import ModelUploadOp
from google_cloud_pipeline_components.types import artifact_types
from google_cloud_pipeline_components.v1.endpoint import EndpointCreateOp, ModelDeployOp
from google_cloud_pipeline_components.v1.hyperparameter_tuning_job import HyperparameterTuningJobRunOp
```

## Advanced Patterns & Orchestration

For specific use-cases, refer to the following guides:

- **Custom Prediction Routines (CPR)**: How to package and serve custom inference logic. See [references/cpr_deployment.md](references/cpr_deployment.md).
- **Hyperparameter Optimization (HPO)**: How to inject Hyperparameter Tuning components into the pipeline graph. See [references/hyperparameter_tuning.md](references/hyperparameter_tuning.md).
- **ML Metadata Tracking**: How to pass `Artifact` and `Dataset` references between steps correctly. See [references/ml_metadata.md](references/ml_metadata.md).

## Pipeline Configuration & Compilation

Always compile the pipeline using the KFP compiler before attempting to submit it to Vertex AI:

```python
@dsl.pipeline(
    name="my-vertex-pipeline",
    description="A demonstration of GCPC components",
    pipeline_root="gs://my-bucket/pipeline_root"
)
def my_pipeline(project: str, location: str):
    # Pipeline steps
    pass

compiler.Compiler().compile(
    pipeline_func=my_pipeline,
    package_path="pipeline.json"
)
```
