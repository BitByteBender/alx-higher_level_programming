-- Displays average tempratures
SELECT city, AVG(*) As avg_temp FROM tempratures
GROUP BY city ORDER BY avg_temp DESC;
