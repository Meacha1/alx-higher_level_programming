-- List the number of records with similar score in the table
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
