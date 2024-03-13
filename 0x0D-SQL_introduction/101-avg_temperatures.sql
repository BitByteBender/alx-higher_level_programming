-- Displays average tempratures
SELECT city, AVG(values) As avg_temp FROM tempratures
GROUP BY city ORDER BY avg_temp DESC;
