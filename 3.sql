-- Найти средний балл в группах по определенному предмету
SELECT d.name as Discipline, AVG(g.grade) as Grade, g2.name as Groupp
From disciplines d LEFT JOIN grades g ON d.id = g.discipline_id
LEFT JOIN students s ON s.id =g.student_id
LEFT JOIN groups g2 ON g2.id =s.groups_id
GROUP BY g2.name, d.name
ORDER BY d.name DESC
