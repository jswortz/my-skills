---
name: timesfm
description: Leverage TimesFM (Time Series Foundation Model) for zero-shot forecasting and anomaly detection on Vertex AI and BigQuery ML.
    Use when analyzing metrics, forecasting future values, or finding anomalies on time-series datasets.
---

# TimesFM (Time Series Foundation Model)

TimesFM is a decoder-only foundation model pre-trained on a massive corpus of time-series data. It is capable of zero-shot forecasting, meaning it can predict future values for unseen datasets without any additional training or fine-tuning.

## Using TimesFM on BigQuery ML

BigQuery ML enables you to create a model directly pointing to the TimesFM architecture.

### 1. Creating the Model

```sql
CREATE OR REPLACE MODEL `my_dataset.my_timesfm_model`
OPTIONS(
  model_type='timesfm'
);
```

### 2. Zero-Shot Forecasting

Use `ML.FORECAST` to generate predictions.

```sql
SELECT *
FROM ML.FORECAST(
  MODEL `my_dataset.my_timesfm_model`,
  TABLE `my_dataset.historical_sales_data`,
  STRUCT(
    30 AS horizon,                   -- Predict next 30 steps
    0.9 AS confidence_level          -- Generates prediction intervals
  )
);
```

### 3. Anomaly Detection

Use `ML.DETECT_ANOMALIES` to find outliers in your historical or incoming data.

```sql
SELECT *
FROM ML.DETECT_ANOMALIES(
  MODEL `my_dataset.my_timesfm_model`,
  STRUCT(0.95 AS anomaly_prob_threshold),
  TABLE `my_dataset.monitoring_data`
);
```

## Advanced Operations & Vertex AI

For more detailed deployments, refer to the following resources:
- **Vertex AI Deployment**: Deploying TimesFM as a custom inference endpoint. See [references/vertex_ai_deployment.md](references/vertex_ai_deployment.md).
- **Core Principles**: Read the foundational concepts at the Google Research blog.
