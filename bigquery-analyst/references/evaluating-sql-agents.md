# Evaluating BigQuery SQL Agents

Evaluating analytical SQL agents requires ensuring they generate correct, performant, and safe queries.

## Evaluation Strategy

1. **Deterministic SQL Validation:** 
   Verify that generated queries are valid BigQuery standard SQL without running them. Use `mcp__bigquery__execute_sql` with `dry_run=True` to check syntax and estimate cost.

2. **Semantic Equivalence:**
   Compare the agent's SQL output to a known "gold standard" query. Since SQL can be written in many ways, check if the output datasets match rather than doing strict string comparison.

3. **Performance Metrics:**
   Evaluate whether the agent applied performance best practices:
   - Are `LIMIT` clauses used for exploratory queries?
   - Are partition filters used appropriately?
   - Are `APPROX_QUANTILES` and `APPROX_COUNT_DISTINCT` used for large tables?

4. **Security & Safety:**
   Ensure the agent is not generating DML or DDL statements unless explicitly requested (e.g., verify queries start with `SELECT` or `WITH`).
