CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        # Write your MySQL query statement below.
        select salary
        from (
            select distinct
                salary,
                dense_rank() over (order by salary desc) as rnk
            from Employee
        ) rnk_table
        where rnk = n
    );
END