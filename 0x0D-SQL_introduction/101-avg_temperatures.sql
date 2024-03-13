-- Displays average tempratures
SELECT city, AVG(value) As avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
