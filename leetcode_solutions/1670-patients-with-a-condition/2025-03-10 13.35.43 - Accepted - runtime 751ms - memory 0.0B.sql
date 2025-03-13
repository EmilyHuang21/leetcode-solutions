# Write your MySQL query statement below
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';

/*
使用 LIKE 判斷
由於 conditions 是由空格分隔的多個代碼，可能出現以下兩種情況：

代碼位於最前面：例如 "DIAB100 MYOP"
→ 使用條件 conditions LIKE 'DIAB1%' 可以匹配。
代碼不在最前面：例如 "ACNE DIAB100"
→ 使用條件 conditions LIKE '% DIAB1%' 可以匹配（注意前面有一個空格）。
篩選條件
使用 OR 將兩個 LIKE 條件結合，即可涵蓋所有情況：

WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'
最終輸出
返回 patient_id、patient_name 以及 conditions 欄位的資料，結果順序可以任意（題目要求 "in any order"）。
*/