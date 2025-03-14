# Write your MySQL query statement below
SELECT 
    ROUND(100 * SUM(order_date = customer_pref_delivery_date) / COUNT(*), 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date) 
    FROM Delivery 
    GROUP BY customer_id
);

/*
Find First Orders:

The subquery SELECT customer_id, MIN(order_date) FROM Delivery GROUP BY customer_id finds the earliest order date for each customer.
We use (customer_id, order_date) IN (...) to filter only those first orders.
Count Immediate Orders:

SUM(order_date = customer_pref_delivery_date) counts the first orders where order_date = customer_pref_delivery_date.
COUNT(*) counts all first orders.
Calculate Percentage:

Multiply by 100 and round to 2 decimal places.
*/