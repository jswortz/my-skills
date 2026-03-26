# BigQuery ML TimesFM Forecasting

BigQuery ML integrates the TimesFM foundation model so you can perform zero-shot forecasting directly on your data warehouse tables using GoogleSQL.

## Creating the Model

Define the model and assign its alias.

```sql
CREATE OR REPLACE MODEL `project_id.dataset_id.timesfm_model`
OPTIONS(
  model_type='timesfm'
);
```

## Forecasting Future Values

Use `ML.FORECAST` to generate future predictions from historical data.

- `horizon`: How many future steps to predict.
- `confidence_level`: The interval width for uncertainty (e.g., 0.90 for 90%).

```sql
SELECT
  *
FROM
  ML.FORECAST(
    MODEL `project_id.dataset_id.timesfm_model`,
    TABLE `project_id.dataset_id.historical_sales`,
    STRUCT(
      14 AS horizon,
      0.95 AS confidence_level
    )
  );
```

### Result Schema

- `forecast_timestamp`: The future time step.
- `forecast_value`: The predicted zero-shot value.
- `prediction_interval_lower_bound`: Lower bound of the confidence interval.
- `prediction_interval_upper_bound`: Upper bound of the confidence interval.

## Detecting Anomalies

Use `ML.DETECT_ANOMALIES` to find outliers in your historical or real-time data using the foundation model's expectations.

```sql
SELECT
  *
FROM
  ML.DETECT_ANOMALIES(
    MODEL `project_id.dataset_id.timesfm_model`,
    STRUCT(0.9 AS anomaly_prob_threshold),
    TABLE `project_id.dataset_id.sensor_data`
  );
```

### Result Schema

- `is_anomaly`: Boolean indicating if the data point deviates significantly.
- `lower_bound` / `upper_bound`: The expected normal range.
- `anomaly_probability`: The probability that this point is an anomaly.
