-- Найти 5 студентов с наибольшим средним баллом по всем предметам
SELECT s.fullname as Student, ROUND (AVG(g.grade), 1) as Average
FROM students s LEFT JOIN grades g ON s.id = g.student_id
GROUP BY g.student_id
ORDER BY Average DESC
LIMIT 5