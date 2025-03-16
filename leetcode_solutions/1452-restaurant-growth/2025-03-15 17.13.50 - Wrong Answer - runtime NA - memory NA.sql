# Write your MySQL query statement below
SELECT 
    c1.visited_on,
    SUM(c2.amount) AS amount,
    ROUND(AVG(c2.amount), 2) AS average_amount
FROM Customer c1
JOIN Customer c2 
    ON c2.visited_on BETWEEN DATE_SUB(c1.visited_on, INTERVAL 6 DAY) AND c1.visited_on
GROUP BY c1.visited_on
HAVING COUNT(DISTINCT c2.visited_on) = 7
ORDER BY c1.visited_on;

/*
JOIN 來計算 7 天內的消費金額

c2.visited_on BETWEEN DATE_SUB(c1.visited_on, INTERVAL 6 DAY) AND c1.visited_on
c1.visited_on 是當前日期。
DATE_SUB(c1.visited_on, INTERVAL 6 DAY) 計算當前日期的 6 天前。
c2.visited_on 代表所有符合這個時間區間的交易。
計算總金額 (SUM(amount)) 和 平均金額 (AVG(amount))

SUM(c2.amount) AS amount 計算這 7 天內的總金額。
ROUND(AVG(c2.amount), 2) AS average_amount 計算 7 天內的平均金額，並四捨五入到 2 位小數。
HAVING COUNT(DISTINCT c2.visited_on) = 7

只選擇 滿 7 天的記錄，確保我們的移動平均是完整的。
ORDER BY c1.visited_on

按照 visited_on 升序排列，確保輸出符合題目要求。
*/