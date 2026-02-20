# Write your MySQL query statement below
select j.name as Customers from
(
    select
        c.id as customerId,
        c.name,
        o.id as orderId
    from Customers c
        Left join Orders o
            on c.id = o.customerId
) as j
where j.orderId is null;