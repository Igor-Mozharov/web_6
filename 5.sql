-- Найти какие курсы читает определенный преподаватель.
SELECT t.fullname as Teacher, d.name as Disciplines
FROM teachers t LEFT JOIN disciplines d ON t.id =d.teachers_id
GROUP BY d.name
ORDER BY d.name DESC