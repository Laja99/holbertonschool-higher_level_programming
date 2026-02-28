-- List all cities
SELECT c.id, c.name, s.name
FROM cities c,
     (SELECT id, name FROM states) s
WHERE c.state_id = s.id
ORDER BY c.id ASC;
