# Write your MySQL query statement below
-- 找出評價最多電影的使用者
SELECT name AS results
FROM Users
JOIN MovieRating ON Users.user_id = MovieRating.user_id
GROUP BY Users.user_id, Users.name
ORDER BY COUNT(MovieRating.movie_id) DESC, name ASC
LIMIT 1

UNION ALL

-- 找出 2020 年 2 月平均評分最高的電影
SELECT title AS results
FROM Movies
JOIN MovieRating ON Movies.movie_id = MovieRating.movie_id
WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY Movies.movie_id, Movies.title
ORDER BY AVG(MovieRating.rating) DESC, title ASC
LIMIT 1;
