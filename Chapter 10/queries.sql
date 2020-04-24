select count(letters) as 'count', letters
from log
group by letters
order by count desc
limit 1;

select distinct ip from log;

select browser_string, count(browser_string) as 'count'
from log
group by browser_string
order by count desc
limit 1;