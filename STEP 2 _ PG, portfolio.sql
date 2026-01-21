# SQL PORTFOLIO — FRAUD & ANOMALY DETECTION
# Author: Patrycja Głuszek
# Environment: BigQuery Sandbox
# Notes: Using public dataset as simulated transactions

# STEP 2 — Merchants with high decline rate
# This simulates a real payments dataset.

WITH transactions AS (
  SELECT
    id AS transaction_id,
    user_id AS customer_id,
    product_id AS merchant_id,
    status,
    created_at AS timestamp,
    sale_price AS amount
  FROM `bigquery-public-data.thelook_ecommerce.order_items`
  WHERE sale_price IS NOT NULL
)

SELECT
  merchant_id,
  COUNTIF(status = 'Cancelled') / COUNT(*) AS decline_rate,
  COUNT(*) AS total_tx
FROM transactions
GROUP BY merchant_id
HAVING decline_rate > 0.25
ORDER BY decline_rate DESC;
