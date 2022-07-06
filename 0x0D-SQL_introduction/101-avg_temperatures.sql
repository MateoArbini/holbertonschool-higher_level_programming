-- script that displays the average temperature (Fahrenheit) by city ordered by
-- temperature (descending).
SELECT AVG(value) as avg_temp
FROM temperatures
ORDER BY avg_temp DESC
