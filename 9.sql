-- Найти список курсов, которые посещает определенный студент
SELECT s.fullname as Student, d.name as Disciplines
From students s LEFT JOIN grades g ON s.id =g.student_id
LEFT JOIN disciplines d ON d.id =g.discipline_id
GROUP BY s.fullname , d.name