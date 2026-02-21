# Write your MySQL query statement below
select
    department as Department,
    employee as Employee,
    salary as Salary
from (
    select
        d.name as department,
        e.name as employee,
        e.salary as salary,
        dense_rank() over (
            partition by d.id
            order by e.salary desc
        ) as rnk
    from Employee as e
        join Department as d
            on d.id = e.departmentId
) as t
where rnk <= 3;