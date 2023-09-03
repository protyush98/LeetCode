# Write your MySQL query statement below
select u.name as name,COALESCE(sum(r.distance),0) as travelled_distance
from Users as u left JOIN Rides as r on u.id=r.user_id
group by u.id
order by travelled_distance desc, name asc;