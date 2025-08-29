SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee AS e JOIN Department AS d
ON e.departmentId = d.id
WHERE e.salary = (
    SELECT MAX(e2.salary)
    FROM Employee AS e2
    WHERE e2.departmentId = e.departmentId
);