SELECT e1.name AS Employee
FROM Employee e1 CROSS JOIN Employee e2
WHERE e1.salary > e2.salary AND e1.managerID = e2.id