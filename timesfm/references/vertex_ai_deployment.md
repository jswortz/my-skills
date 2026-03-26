# Operationalizing TimesFM on Vertex AI

While BigQuery ML provides the easiest interface for TimesFM, you can deploy the open-weight release of TimesFM to a dedicated Vertex AI Endpoint (e.g., L4 GPUs) for real-time inference or low-latency applications.

## Deployment Architecture

1.  **Model Image**: Use a pre-built Deep Learning VM container serving TimesFM, or build a custom `vLLM`/`TGI` container.
2.  **Upload to Vertex Model Registry**: Register the container image with the required hardware specifications.
3.  **Deploy to Endpoint**: Provision backend resources (e.g., NVIDIA L4 GPUs).

```python
from google.cloud import aiplatform

aiplatform.init(project="my-project", location="us-central1")

# Assuming a custom serving container is built for TimesFM
model = aiplatform.Model.upload(
    display_name="timesfm-1.0-200m",
    serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.1-13:latest",
    serving_container_predict_route="/predict",
    serving_container_health_route="/health"
)

# Deploy to a GPU endpoint
endpoint = model.deploy(
    machine_type="g2-standard-4",
    accelerator_type="NVIDIA_L4",
    accelerator_count=1
)

# Querying the endpoint
prediction = endpoint.predict(instances=[
    # Time-series context data
    {"sequence": [1.0, 2.0, 3.0, 4.0, 5.0]}
])
print(prediction)
```
