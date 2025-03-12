# Write your MySQL query statement below
DELETE p1
FROM Person p1
JOIN Person p2 ON p1.email = p2.email
WHERE p1.id > p2.id;

/*
目標：

刪除所有重複的 email，只保留每個 email 最小 id 的那一行。
自我連接 (Self-Join)：

使用 JOIN 連接同一張表，令 p1 與 p2 的 email 相同。
條件 p1.id > p2.id 用來確定 p1 為重複記錄中 id 較大的那一筆，而 p2 為較小的那一筆。
DELETE 操作：

透過 DELETE p1 刪除重複記錄中 id 較大的那些行，從而只保留每個 email 最小 id 的那一筆。
*/