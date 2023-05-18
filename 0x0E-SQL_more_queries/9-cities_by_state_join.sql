-- cities by id

select cities.id, cities.name, states.name
from cities
join states on states.id = cities.state_id
order by cities.id asc;
