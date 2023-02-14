-- Display the highest temperature of each state sorted by the name of the state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
