-- script that list the number of records

SELECT `score`, COUNT(*) as `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
