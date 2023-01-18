-- Найти список студентов в определенной группе
SELECT s.fullname as Student, g.name as Groupp
FROM students s LEFT JOIN groups g ON s.groups_id =g.id
GROUP BY s.fullname
ORDER BY g.name ASC