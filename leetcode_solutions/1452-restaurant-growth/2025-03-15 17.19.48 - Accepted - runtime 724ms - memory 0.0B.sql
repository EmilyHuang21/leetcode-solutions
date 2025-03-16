WITH Daily_Sum AS (
    SELECT visited_on, SUM(amount) AS total_amount
    FROM Customer
    GROUP BY visited_on
),
Moving_Avg AS (
    SELECT d1.visited_on, 
           SUM(d2.total_amount) AS amount, 
           ROUND(AVG(d2.total_amount) OVER (ORDER BY d1.visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
    FROM Daily_Sum d1
    JOIN Daily_Sum d2
    ON d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY) AND d1.visited_on
    GROUP BY d1.visited_on
)
SELECT visited_on, amount, average_amount
FROM Moving_Avg
WHERE visited_on >= (SELECT MIN(visited_on) + INTERVAL 6 DAY FROM Customer)
ORDER BY visited_on;
