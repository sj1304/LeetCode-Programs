# Write your MySQL query statement below
select w1.id FROM weather w1 join weather w2 on datediff(w2.recorddate,w1.recorddate)=-1
where w2.temperature<w1.temperature