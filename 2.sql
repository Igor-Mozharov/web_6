-- Найти студента с наивысшим средним баллом по определенному предмету.
SELECT d.name as Discipline, ROUND (AVG(g.grade), 2) as Average, s.fullname as Student
FROM disciplines d LEFT JOIN grades g ON g.discipline_id =d.id
LEFT JOIN students s ON g.student_id =s.id
GROUP BY d.name
ORDER BY Average DESC 