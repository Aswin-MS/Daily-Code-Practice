use sample3;
select *from customer1;
select fname,lname,age,prof from customer1 limit 30;
select fname,lname,age from customer1 limit 10;
create view dat as select fname,lname,age,prof from customer1;
select * from dat;
select fname,lname,age,prof from customer1 where age>50;
select fname,lname,age,prof,loc from customer1 where age>=25 and age<=40;
select fname,lname,age,prof from customer1 where loc='india';
select fname,lname,age from customer1 where loc='india' order by age limit 3;
create view dat1 as select fname,lname,age,prof from customer1 where loc='india' and prof='Doctor' order by age desc limit 1;
select * from dat1;
select fname,lname,age,prof from customer1 where loc='uk' order by age desc limit 10;
create view dat2 as select fname,lname,age,prof from customer1 where loc='us' and age>60;
select * from dat2;
create view dat3 as select fname,lname,age from customer1 where prof='Pilot' order by age desc limit 3;
select * from dat3;
select * from customer1 where prof='Pilot' order by age limit 1;
select count(*) from customer1;
select prof,count(*) as count from customer1 group by prof order by count desc;
select prof,count(*) as count from customer1 where loc='india' group by prof order by count desc;

#ASSIGNMENT
#q1
select count(*) from customer1;
#q2
create view uni as select distinct * from customer1;
select * from uni;
select count(*) from uni;
#q3
select fname,lname,prof,loc from customer1 order by age desc limit 10;
#q4
select fname,lname,prof,loc from customer1 order by age  limit 5;
#q5
select loc,count(*) as count from customer1 group by loc order by count desc;
#q6
select * from customer1 where loc='australia';
#q7
select age,count(*) as total from customer1 group by age order by total desc;
#q8
select prof,count(*) as total from customer1 group by prof order by total desc;
#q9:
#A:
select count(*) from customer1 where loc='india';
#B:
select prof,count(*) as total from customer1  where loc='india' group by prof order by total desc;
#C:
select fname,lname,age,prof from customer1 where loc='india' order by age desc limit 3;
#D:
select fname,lname,age,prof from customer1 where loc='india' order by age limit 3;
#E:
select * from customer1 where loc='india' and age>40;
#F:
select prof,count(*) from customer1 where loc='india' and 30<=age<=40 group by prof order by count(*) desc;
#q10:
create view us as select * from customer1 where loc='us';
select * from us;
#A:
select count(*) from us;
#B:
select age,count(*) as total from us group by age order by total desc;
#C:
select prof,count(*) as total from us group by prof order by total;
#D:
select * from us where prof='Civil engineer' and age>30;
