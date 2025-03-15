# Write your MySQL query statement below
WITH ProductCount AS (
    SELECT COUNT(*) AS total_products FROM Product
)
SELECT c.customer_id
FROM Customer c
GROUP BY c.customer_id
HAVING COUNT(DISTINCT c.product_key) = (SELECT total_products FROM ProductCount);

/*
Count the total number of unique products in the Product table using a Common Table Expression (CTE) ProductCount.
Group the Customer table by customer_id and count the distinct product_key values for each customer.
Use the HAVING clause to filter customers whose count of distinct products matches the total number of products in the Product table.
*/