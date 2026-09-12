# Write your MySQL query statement below
select d.name as Department, e.name as Employee, e.salary as Salary
from Employee e
left join Department d
on d.id = e.departmentId
where (d.id, e.salary) in
(select departmentId, max(salary)
from employee
group by departmentId)


