-- Display the max temperature of each state in ascending order of state name
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
