select id, max(length) as length
from FISH_INFO
where length is not NULL
group by id
order by max(length) desc, id asc
limit 10;