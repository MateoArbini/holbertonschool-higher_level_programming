-- script that displays the max temo of each stat, order by state name
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC
LIMIT 3
