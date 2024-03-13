-- Lists all recs of second_table
SELECT score, name FROM second_table WHERE name != '' ORDER BY score DESC, name DESC;
