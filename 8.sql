-- Найти средний балл, который ставит определенный преподаватель по своим предметам
SELECT t.fullname as Teacher, d.name as Discipline, ROUND(AVG(g.grade), 2) as Grade
FROM teachers t LEFT JOIN disciplines d ON t.id =d.teachers_id
LEFT JOIN grades g ON g.discipline_id =d.id
GROUP BY d.name
ORDER BY d.name DESC