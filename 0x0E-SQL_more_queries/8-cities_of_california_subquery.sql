-- script that lists all cities found in a db

SELECT id, name from cities where state_id = (select id from states where name = "california") order by id ASC;
