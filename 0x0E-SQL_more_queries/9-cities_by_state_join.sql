-- Lists all cities contained in the database hbtn_0d_usa.
-- Selects all cities with their corresponding state names from the hbtn_0d_usa database.
SELECT CONCAT(cities.id, ' - ', cities.name, ' - ', states.name) AS result
FROM cities, states WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
