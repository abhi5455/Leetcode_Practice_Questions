SELECT Max(salary) AS SecondHighestSalary
FROM Employee
WHERE salary NOT IN (
    SELECT Max(salary) AS salary
    FROM Employee
);