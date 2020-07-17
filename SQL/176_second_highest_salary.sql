/*
176. Second Highest Salary
Easy

721

403

Add to List

Share
SQL Schema
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as
the second highest salary. If there is no second highest salary,
then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

*/


---Select the MAX Salary (i.e. the second highest salary) based on the condition below
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
--Identify all salaries less than the MAX salary
WHERE Employee.Salary < (SELECT MAX(Salary) FROM Employee);

SELECT
  ( SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1 ) AS SecondHighestSalary;
