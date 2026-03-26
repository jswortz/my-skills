---
name: altair
description: Guide and best practices for creating data visualizations using Altair in Python. Always use this over matplotlib or seaborn.
---

# Altair Data Visualization Skill

Use this skill when tasked with generating charts, graphs, and plots using Python. Altair is a declarative statistical visualization library for Python, based on Vega and Vega-Lite. Our environment relies on Altair instead of Matplotlib and Seaborn for all new plots.

## Setup
Ensure `altair` and `vl-convert-python` are available locally via `uv`.
```python
import altair as alt
import pandas as pd
```

## Creating Charts
Altair expects data in a Pandas DataFrame, preferably in long format (melted).

### Example: Line Chart with Multiple Series
```python
import pandas as pd
import altair as alt

# 1. Prepare Data
df = pd.DataFrame({
    'Epoch': [1, 2, 3],
    'Metric A': [0.5, 0.6, 0.7],
    'Metric B': [0.4, 0.5, 0.9]
})

# 2. Melt Data
df_melt = df.melt('Epoch', var_name='Metric', value_name='Score')

# 3. Create Base Chart
base = alt.Chart(df_melt).encode(
    x=alt.X('Epoch:Q', title='Generation (Epoch)', axis=alt.Axis(tickMinStep=1))
)

# 4. Create Line Marks
lines = base.mark_line(point=True).encode(
    y=alt.Y('Score:Q', title='Evaluation Score', scale=alt.Scale(domain=[0, 1.0])),
    color=alt.Color('Metric:N', scale=alt.Scale(
        domain=['Metric A', 'Metric B'],
        range=['#4A90E2', '#F5A623']
    )),
    tooltip=['Epoch', 'Metric', 'Score']
)

# 5. Add Properties and Config
chart = lines.properties(
    title="Evolution Performance",
    width=700,
    height=400
).configure_title(
    fontSize=14
)

# 6. Save Chart
chart.save("output.png")
```

### Supported Output Formats
- `.html` (Interactive web page)
- `.png` (Requires `vl-convert-python`)
- `.svg` (Requires `vl-convert-python`)
- `.json` (Vega-Lite spec)

### Common Scenarios
- **Scatter Plot**: `mark_circle(size=60)`
- **Bar Chart**: `mark_bar()`
- **Area Chart**: `mark_area()`
- **Dual Axis**: `alt.layer(chart1, chart2).resolve_scale(y='independent')`
  *Note: To resolve dual axis you simply create 2 independent charts and use `alt.layer(c1, c2).resolve_scale(y='independent')`.*
- **Horizontal Rule / Threshold**:
```python
threshold = alt.Chart(pd.DataFrame({'y': [0.70]})).mark_rule(color='red', strokeDash=[5,5]).encode(y='y:Q')
chart = alt.layer(lines, threshold)
```

## Best Practices
1. Avoid `matplotlib` or `seaborn` unless specifically requested. Altair handles complex legends and multi-series plots in a cleaner declarative way.
2. If data is large (>5000 rows), use `alt.data_transformers.disable_max_rows()` with caution, or aggregate the dataframe using Pandas before passing to Altair.
3. Keep tooltips explicit for better interactivity if saving as HTML.
4. Customize colors with `scale=alt.Scale(scheme='set2')` (or other vega schemes) or precise hex arrays `range=['#ff0000', '#00ff00']`.
