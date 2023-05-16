-- list tables and displays average

SELECT city, AVG(value) avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
