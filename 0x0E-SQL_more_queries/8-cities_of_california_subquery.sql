-- lists all cali cities that can be found in hbtn_0d_usa db
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "california")
ORDER BY id ASC;
