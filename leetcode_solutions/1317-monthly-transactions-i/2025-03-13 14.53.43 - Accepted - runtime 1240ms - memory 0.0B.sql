# Write your MySQL query statement below
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY month, country;

/*
Extract Month: DATE_FORMAT(trans_date, '%Y-%m') AS month extracts the year and month from trans_date.
Grouping: The query groups transactions by month and country.
Counting Transactions: COUNT(*) AS trans_count counts total transactions per group.
Counting Approved Transactions: SUM(state = 'approved') AS approved_count counts only the "approved" transactions.
Total Transaction Amount: SUM(amount) AS trans_total_amount calculates the total transaction amount.
Total Approved Transaction Amount: SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount sums only approved transaction amounts.
*/