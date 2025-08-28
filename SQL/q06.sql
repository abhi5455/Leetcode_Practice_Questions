SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM SalesPerson AS s JOIN Company AS c JOIN Orders AS o
    ON o.sales_id = s.sales_id AND o.com_id = c.com_id
    WHERE c.name = 'RED'
);