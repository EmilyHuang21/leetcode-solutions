# Write your MySQL query statement below
WITH LatestPrices AS (
    SELECT product_id, new_price, change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT p.product_id, 
       COALESCE(lp.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN LatestPrices lp
ON p.product_id = lp.product_id 
AND lp.change_date = (SELECT MAX(change_date) 
                      FROM LatestPrices 
                      WHERE product_id = p.product_id);

/*
找出 2019-08-16 當天或之前的最新價格

需要找出 change_date <= '2019-08-16' 的最大 change_date。
若某產品 沒有記錄，則價格為 10。
使用 LEFT JOIN 或 MAX(change_date) 來獲取最新價格

MAX(change_date) 幫助我們獲取最近一次的價格變更。
若沒有變更記錄，則價格設為 10。

WITH LatestPrices AS (...)

過濾出 2019-08-16 及之前的價格變更記錄 (WHERE change_date <= '2019-08-16')。
(SELECT DISTINCT product_id FROM Products)

找出所有 曾經發生價格變更 的 product_id。
LEFT JOIN 來匹配最新價格

MAX(change_date) 找到 該 product_id 在 2019-08-16 當天或之前的最新價格。
COALESCE(lp.new_price, 10)
如果 lp.new_price 為 NULL（表示此產品沒有變更過價格），則 預設價格為 10。
*/