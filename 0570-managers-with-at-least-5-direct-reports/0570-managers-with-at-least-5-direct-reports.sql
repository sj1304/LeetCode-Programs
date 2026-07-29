# Write your MySQL query statement below
Select p1.name
FROM Employee p1 JOIN Employee p2 ON p1.id=p2.managerId 
GROUP BY p1.id
Having count(p2.managerId)>=5