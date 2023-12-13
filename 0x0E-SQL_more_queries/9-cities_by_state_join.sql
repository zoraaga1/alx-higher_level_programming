-- Lists all cities contained in the database hbtn_0d_usa.
-- Selects all cities with their corresponding state names from the hbtn_0d_usa database.
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
