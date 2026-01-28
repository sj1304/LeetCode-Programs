# Write your MySQL query statement below
select p.product_name,s.year,s.price from Sales s,Product p where s.product_id in(select p.product_id from Product);