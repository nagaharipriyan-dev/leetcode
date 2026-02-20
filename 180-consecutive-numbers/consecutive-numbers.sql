# Write your MySQL query statement below
select distinct num as ConsecutiveNums from (
    select num,
        lag(num, 1) over (order by id) as prev,
        lead(num, 1) over (order by id) as next
    from Logs
) t where prev = num and next = num;