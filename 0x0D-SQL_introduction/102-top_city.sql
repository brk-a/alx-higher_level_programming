-- Display the top 3 cities' avg temperatures during July and August in descending order of temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures
  WHERE month = 7 OR month = 8
  GROUP BY city
  ORDER BY avg_temp DESC LIMIT 3;
