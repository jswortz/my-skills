# ML Metadata in Vertex AI Pipelines

ML Metadata tracks the inputs and outputs of each step in a Vertex AI Pipeline. This provides full lineage for artifacts like datasets, models, metrics, and custom visualizations.

## Declaring Inputs and Outputs

Components in `kfp.v2.dsl` accept `Input[Type]` and `Output[Type]` annotations. Types include `Dataset`, `Model`, `Metrics`, `HTML`, `Markdown`, etc.

### Metadata Logging Example

```python
import kfp
from kfp.dsl import component, Input, Output, Dataset, Metrics, Model

@component()
def train_model(
    dataset: Input[Dataset],
    model: Output[Model],
    metrics: Output[Metrics]
):
    import json
    
    # 1. Read input dataset
    with open(dataset.path, 'r') as f:
        data = f.read()
    
    # 2. Train your model
    # model.uri provides the GCS path Vertex allocated for this output
    
    # 3. Log metrics to Vertex ML Metadata
    metrics.log_metric("accuracy", 0.95)
    metrics.log_metric("f1_score", 0.92)

    # 4. Save model artifact
    # Vertex Pipelines will automatically track this `model` artifact in Metadata
    with open(model.path, 'w') as f:
        f.write("mock_model_weights")
```

### Passing Artifacts Between Steps

Artifacts are passed as regular function arguments in your pipeline definition. Vertex AI resolves the GCS paths automatically.

```python
@dsl.pipeline(name="ml-metadata-pipeline")
def metadata_pipeline():
    # component_a outputs a Dataset
    data_gen = generate_data_op()
    
    # Pass the output dataset directly as an input to component_b
    train_task = train_model_op(
        dataset=data_gen.outputs["output_dataset"]
    )
```
