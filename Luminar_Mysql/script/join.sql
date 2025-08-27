create database joinn;
use joinn;
show tables;
select * from tb1;
select * from tb2;
desc tb2;
select one.name,one.age,one.location,one.salary,two.dat,two.amount from tb1 one join tb2 two on(one.id=two.id) ;
select a.*,b.dat,b.amount from tb1 a join tb2 b on(a.id=b.id);
select a.name,a.age,a.salary,b.dat,b.amount from tb1 a join tb2 b on(a.id=b.id) where a.salary>6000;
select a.name,a.age,a.salary,b.dat,b.amount from tb1 a join tb2 b on(a.id=b.id) order by a.age desc limit 1;
select a.name,a.age,a.location,a.salary,b.dat,b.amount from tb1 a join tb2 b on(a.id=b.id) order by a.age  limit 1;
select a.name,a.age,a.salary,b.dat,b.amount from tb1 a join tb2 b on(a.id=b.id) order by b.dat desc limit 1;
select * from result;
select student.*,result.res from student join result on(student.roll=result.roll) where result.res='pass' ;

#LEFT JOIN
select a.name,a.age,a.location,a.salary,b.dat,b.amount from tb1 a left join tb2 b on(a.id=b.id);
#RIGHT JOIN
select b.dat,b.amount,a.name,a.age,a.location,a.salary from tb1 a right join tb2 b on(a.id=b.id);
#FULL JOIN
select a.name,a.age,a.location,a.salary,b.dat,b.amount from tb1 a left join tb2 b on(a.id=b.id) union select a.name,a.age,a.location,a.salary,b.dat,b.amount from tb1 a right join tb2 b on(a.id=b.id);

