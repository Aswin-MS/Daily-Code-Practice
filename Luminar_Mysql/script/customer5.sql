use sample3;
select * from customer5;
select count(*) from customer5;
select prof,count(*) as total from customer5 group by prof order by total desc;
select prof,sum(salary) as total from customer5 group by prof order by total desc;
select loc,max(age) as max_age from customer5 group by loc order by max_age desc;
select prof,min(salary) from customer5 group by prof order by min(salary) desc;
select loc,avg(age) as avg_age from customer5 group by loc order by avg_age desc;
select prof,max(salary) as max from customer5 where loc='india' group by prof order by max desc;

