# Write your MySQL query statement below
SELECT name AS Employee FROM Employee e1 WHERE salary > (SELECT salary FROM Employee e2 WHERE e1.managerId = e2.Id and e1.salary > e2.salary)


#------------------------------------------------------------
