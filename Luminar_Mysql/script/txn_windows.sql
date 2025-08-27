create database sample4;
use sample4;
select * from txn_windows;
#ASSIGNMENT 2
#q1
select count(*) from txn_windows;
#q2
create view jan as select oid,cuid,category,product,state from txn_windows where dat like '01-%-2011' ;
select * from jan;
#q2A
select count(*) from jan;
#q3
create view jul as select oid,cuid,category,product,state from txn_windows where dat like '07-%-2011' ;
select * from jul;
#q3A
select count(*) from jul;
#q4
select category,count(*) as count from txn_windows group by category order by count desc;
#q5
select * from txn_windows where category='Outdoor Recreation';
#q6
select method,count(*) as count from txn_windows group by method order by count ;
#q7
create view q7 as select * from txn_windows where dat between '01-01-2011' and '07-31-2011';
select * from q7;
select count(*) as purchase_count from q7;
#q8
select category,sum(pay_amount) from txn_windows group by category;
#q9
select category,max(pay_amount) from txn_windows group by category;
#q10
select category,avg(pay_amount) from txn_windows group by category;
#q11
select method,sum(pay_amount) from txn_windows group by method;
#q12
select category,sum(pay_amount) from txn_windows where category='Indoor Games' group by category;
#q13
select state,count(*) from txn_windows group by state order by count(*) desc;