-- Список курсов, которые определенному студенту читает определенный преподаватель.
SELECT s.fullname as Student, t.fullname as Teacher, d.name as Discipline
FROM students s LEFT JOIN grades g ON s.id =g.student_id
LEFT JOIN disciplines d ON g.discipline_id =d.id
LEFT JOIN teachers t ON d.teachers_id =t.id
GROUP BY d.name, s.fullname