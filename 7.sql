-- Найти оценки студентов в отдельной группе по определенному предмету.
SELECT s.fullname as Student, g.name as Groupp, d.name as Discipline, g2.grade as Grade
FROM groups g LEFT JOIN students s ON g.id =s.groups_id
LEFT JOIN grades g2 ON g2.student_id =s.id
LEFT JOIN disciplines d ON d.id =g2.discipline_id
GROUP BY g2.id
ORDER BY g2.grade DESC, d.name ASC