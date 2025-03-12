# Write your MySQL query statement below
SELECT employee_id,
       CASE 
         WHEN SUM(CASE WHEN primary_flag = 'Y' THEN 1 ELSE 0 END) > 0 
           THEN MAX(CASE WHEN primary_flag = 'Y' THEN department_id END)
         ELSE MAX(department_id)
       END AS department_id
FROM Employee
GROUP BY employee_id
ORDER BY employee_id;
/*
目的
當員工屬於多個部門時，必定有一筆資料的 primary_flag 為 'Y'，我們需要返回該部門。
當員工只屬於一個部門時，該筆資料的 primary_flag 為 'N'，我們也需要返回這個部門。


我們對每個 employee_id 進行分組（GROUP BY employee_id）。
使用內嵌的 CASE WHEN 計算該員工有多少筆 primary_flag = 'Y' 的記錄：
SUM(CASE WHEN primary_flag = 'Y' THEN 1 ELSE 0 END)：如果這個總和大於 0，表示該員工有設定 primary 部門。
若存在 primary 部門（primary_flag = 'Y' 的記錄），則用 MAX(CASE WHEN primary_flag = 'Y' THEN department_id END) 返回該部門的 department_id。
如果不存在（也就是該員工只有一筆部門記錄），則返回 MAX(department_id)（實際上只有一個值）。
*/