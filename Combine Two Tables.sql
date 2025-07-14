# Write your MySQL query statement below
SELECT firstName,lastName,city,state FROM Person Left JOIN Address ON Person.personId = Address.personId