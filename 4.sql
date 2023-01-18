-- Найти средний балл на потоке (по всей таблице оценок).
SELECT ROUND(AVG(grades.grade), 2) as average_value
FROM grades