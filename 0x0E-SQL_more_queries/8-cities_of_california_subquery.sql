-- script that list cities of california 
-- list all rows

SELECT id, name FROM cities where state_id = (select id from states where name = 'california') ORDER BY id asc;
