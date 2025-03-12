# Write your MySQL query statement below
SELECT user_id,
       CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;

/*
UPPER(LEFT(name, 1))
取得 name 的第一個字符，並轉換成大寫。
LOWER(SUBSTRING(name, 2))
從第二個字符開始取得 name 的其餘部分，並轉換成小寫。
CONCAT(...)
將上述兩部分連接起來，形成正確格式的名字（首字母大寫，其餘字母小寫）。
ORDER BY user_id
依照 user_id 升序排列結果。
*/