# Write your MySQL query statement below
SELECT 
    ROUND(
        COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2
    ) AS fraction
FROM Activity 
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) 
      IN (SELECT player_id, MIN(event_date) FROM Activity GROUP BY player_id);

/*
Find First Login Date:

The subquery SELECT player_id, MIN(event_date) FROM Activity GROUP BY player_id gets the first login date for each player.
Check Next-Day Login:

We filter Activity where (player_id, previous day’s event_date) matches (player_id, first login date), meaning the player logged in the next day.
Count and Compute Fraction:

COUNT(DISTINCT player_id) counts players who logged in the next day.
SELECT COUNT(DISTINCT player_id) FROM Activity counts total unique players.
The fraction is calculated and rounded to 2 decimal places.
*/
