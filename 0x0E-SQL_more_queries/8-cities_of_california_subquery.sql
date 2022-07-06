-- script that lists all the cities of California that can be found in the
-- database hbtn_0d_usa. The states table contains only one record where
-- name = California (but the id can be different, as per the example) Results
-- must be sorted in ascending order by cities.id Join not allowed.
SELECT cities
FROM hbtn_0d_usa
WHERE cities.id (
	SELECT cities
	FROM hbtn_0d_usa
	WHERE name = "California");
