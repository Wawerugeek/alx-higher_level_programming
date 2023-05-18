-- script that lists all cities found in a db

SELECT cities.id, cities.name from cities
where state_id = (
	select id from states where name = 'california'
)
order by cities.id asc;
