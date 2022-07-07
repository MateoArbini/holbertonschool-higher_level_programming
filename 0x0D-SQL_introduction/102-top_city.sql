-- display top 3 of cities temperatures during July and August order by DESC
SELECT temperatures.city as cities, AVG(temperatures.value) as avg_temp
FROM temperatures
WHERE month = "July" OR month = "August"
GROUP BY city
ORDER BY avg_temp DESC
