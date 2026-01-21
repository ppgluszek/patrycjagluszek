# SQL PORTFOLIO — FRAUD & ANOMALY DETECTION
# Author: Patrycja Głuszek
# Environment: BigQuery Sandbox
# Notes: Using public dataset as simulated transactions

# STEP 3 — Velocity check (multiple transactions in short time)
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
  customer_id,
  COUNT(*) AS tx_count,
  MIN(timestamp) AS first_tx,
  MAX(timestamp) AS last_tx,
  TIMESTAMP_DIFF(MAX(timestamp), MIN(timestamp), MINUTE) AS minutes_between
FROM transactions
GROUP BY customer_id
HAVING tx_count >= 3
   AND minutes_between <= 10
ORDER BY tx_count DESC;
