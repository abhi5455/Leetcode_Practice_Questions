DELETE p1
FROM Person p1
JOIN Person p2
WHERE p1.email = p2.email AND p1.id > p2.id;

-- Another Solution

-- DELETE
-- FROM Person
-- WHERE id NOT IN (
--     SELECT id
--     FROM (
--         SELECT Min(id) as id, email
--         FROM Person
--         GROUP BY email
--     ) as subq
-- )