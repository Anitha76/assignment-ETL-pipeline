-- Top 10 Selling Products

SELECT product_id,
SUM(total_revenue) AS revenue
FROM fact_sales
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;


-- Monthly Revenue
SELECT
DATE_TRUNC('month', order_date) AS month,
SUM(total_revenue) AS revenue
FROM fact_sales
GROUP BY month
ORDER BY month;

-- Customer Purchase Frequency (Region Based)
SELECT
customer_region,
COUNT(order_id) AS purchase_count
FROM fact_sales
GROUP BY customer_region
ORDER BY purchase_count DESC;