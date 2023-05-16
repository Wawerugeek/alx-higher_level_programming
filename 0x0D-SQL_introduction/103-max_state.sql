-- display max temp

SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state asc;
