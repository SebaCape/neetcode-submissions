-- Write your query below
SELECT DISTINCT customer_id
FROM customers AS cust
WHERE cust.year = 2020 AND cust.revenue > 0;