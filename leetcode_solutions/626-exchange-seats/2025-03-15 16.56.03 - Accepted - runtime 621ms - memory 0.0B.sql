# Write your MySQL query statement below
SELECT 
    CASE 
        WHEN MOD(id, 2) = 1 AND id + 1 <= (SELECT MAX(id) FROM Seat) THEN id + 1
        WHEN MOD(id, 2) = 0 THEN id - 1
        ELSE id
    END AS id, 
    student
FROM Seat
ORDER BY id;

/*
1️⃣ 使用 MOD(id, 2) 判斷 id 是奇數還是偶數
MOD(id, 2) = 1 → id 是 奇數（如 1, 3, 5）。
MOD(id, 2) = 0 → id 是 偶數（如 2, 4, 6）。
2️⃣ 如果 id 是奇數 (MOD(id, 2) = 1)
id + 1：將 id 增加 1，與下一行的 id 交換。
但要確保 id + 1 不超過最大 id，因為如果 id 是最後一行（總數為奇數），則 不交換。
條件：id + 1 <= (SELECT MAX(id) FROM Seat)
這確保 id 不是最後一行，例如 id = 5 時，不要加 1，否則超出範圍。
3️⃣ 如果 id 是偶數 (MOD(id, 2) = 0)
id - 1：將 id 減少 1，與前一行的 id 交換。
4️⃣ 如果 id 是最後一個（總數為奇數）
ELSE id：保持不變。
5️⃣ 使用 ORDER BY id
這確保輸出結果按照 id 升序排列，因為 CASE 會改變 id 值，但 ORDER BY 會讓它回到正確的順序。
*/