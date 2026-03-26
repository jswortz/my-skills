# Custom Prediction Routines (CPR)

When deploying custom models to Vertex AI, you frequently need a Custom Prediction Routine (CPR) to handle pre-processing, inference, and post-processing correctly inside a single container, bypassing the default framework servers.

## Workflow

1.  **Develop the Predictor**: Extend `google.cloud.aiplatform.prediction.Predictor`.
2.  **Package**: Use `aiplatform.LocalModel.build_cpr_model()` to containerize it.
3.  **Upload & Deploy**: Push to the registry and create an endpoint.

### Example Predictor

```python
from google.cloud.aiplatform.prediction import Predictor
from google.cloud.aiplatform.utils import prediction_utils

class MyPredictor(Predictor):
    def __init__(self):
        pass

    def load(self, artifacts_uri: str):
        # Load weights or assets here
        pass

    def predict(self, instances):
        # Add pre-processing, inference, and post-processing
        return {"predictions": [f"Processed: {i}" for i in instances]}
```

### Build & Deploy in Code

```python
from google.cloud import aiplatform

aiplatform.init(project="my-project", location="us-central1")

local_model = aiplatform.LocalModel.build_cpr_model(
    "{YOUR_SRC_DIR}",
    f"{REGION}-docker.pkg.dev/{PROJECT_ID}/{REPOSITORY}/{IMAGE}",
    predictor=MyPredictor,
    requirements_path="requirements.txt",
)

local_model.push_image()

model = aiplatform.Model.upload(
    local_model=local_model,
    display_name="my-cpr-model",
)

endpoint = model.deploy(machine_type="n1-standard-4")
```
