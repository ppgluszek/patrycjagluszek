# SQL PORTFOLIO — Transaction Anomaly Detection (SQL Project)
# Author: Patrycja Głuszek
# Environment: BigQuery Sandbox
# Notes: Using public dataset as simulated transactions

# STEP 1 — CREATE A VIRTUAL TRANSACTIONS TABLE (CTE)
# This simulates a real payments dataset.

WITH transactions AS (
  SELECT
    id AS transaction_id,
    user_id AS customer_id,
    product_id AS merchant_id,
    status,
    created_at AS timestamp,
    sale_price AS amount,
    'US' AS country
  FROM `bigquery-public-data.thelook_ecommerce.order_items`
  WHERE sale_price IS NOT NULL
),

stats AS (
  SELECT
    APPROX_QUANTILES(amount, 100)[OFFSET(95)] AS p95
  FROM transactions
)

SELECT
  t.*
FROM transactions t
WHERE t.amount > (SELECT p95 FROM stats)
ORDER BY t.amount DESC;
