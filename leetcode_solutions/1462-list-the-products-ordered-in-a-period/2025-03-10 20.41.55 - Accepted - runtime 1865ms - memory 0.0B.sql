# Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) AS unit
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100;

/*
資料來源與連接

我們有兩個表：Products（包含產品資訊）和 Orders（包含訂單資訊）。
使用 JOIN 將兩個表根據 product_id 連接，這樣可以取得產品的名稱（product_name）。
過濾日期範圍

我們只需要 2020 年 2 月的訂單。
條件 WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29' 用來過濾出 2020 年 2 月的訂單。
分組與計算總數

使用 GROUP BY p.product_id, p.product_name 依據產品進行分組。
使用 SUM(o.unit) 計算每個產品在 2020 年 2 月的總訂購數量。
篩選訂單數量

只有那些在 2020 年 2 月總訂單數量 至少 100 的產品才需要返回。
使用 HAVING SUM(o.unit) >= 100 來達成此要求。
返回欄位

最後返回 product_name 和對應的總訂購數量（命名為 unit）。
*/