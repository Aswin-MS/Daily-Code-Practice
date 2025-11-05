#ASSIGNMENT 3
create database movie;
use movie;
create table distribution_companies(id int primary key,company_name varchar(30));
desc distribution_companies;
create table movies(id int, movie_title varchar(30),imdb_rating float,year_released int,budget double,box_office double,distribution_company_id int,language varchar(20), foreign key(distribution_company_id) references distribution_companies(id));
desc movies;
insert into distribution_companies(id,company_name) values(1,'Columbia Pictures');
select * from distribution_companies;
insert into distribution_companies(id,company_name) values(2,'Paramount Pictures'),(3,'Warner bros. Pictures'),(4,'United Artists'),(5,'Universal Pictures'),(6,'New Line Cinema'),(7,'Miramax Films'),(8,'Produzioni Europee Associate'),(9,'Buena Vista');
select * from distribution_companies;
insert into movies(id,movie_title,imdb_rating,year_released,budget,box_office,distribution_company_id,language) values(1,'The Shawshank Rededmption',9.2,1994,25.00,73.30,1,'English');
select * from movies;
insert into movies(id,movie_title,imdb_rating,year_released,budget,box_office,distribution_company_id,language) values(2,'The Godfather',9.2,1972,7.20,291.00,2,'English');
insert into movies(id,movie_title,imdb_rating,year_released,budget,box_office,distribution_company_id,language) values(3,'The Dark Knight',9.0,2008,185.00,1006.00,3,'English'),(4,'the Godfather Part 2',9.0,1974,13.00,93.00,2,'English,Sicilian'),(5,'12 Angry Men',9.0,1957,0.34,2.00,4,'English');
insert into movies(id,movie_title,imdb_rating,year_released,budget,box_office,distribution_company_id,language) values(6,"Schindler's List",8.9,1993,22.00,322.20,5,'English,German,Yiddish');
select * from movies;
alter table movies modify language varchar(40);
#Q1
select *from distribution_companies;
#Q2
select movie_title,imdb_rating,year_released from movies;
#Q3
select movie_title,box_office from movies where box_office>300;
#Q4
select movie_title,imdb_rating,year_released from movies where movie_title like '%Godfather%';
#Q5
select movie_title,imdb_rating,year_released from movies where year_released<2001 and imdb_rating>9;
#Q6
select movie_title,imdb_rating,year_released from movies where year_released>1991 order by year_released;
#Q7
select language,count(*) from movies group by language;
#Q8
select year_released,count(*) as total_movies from movies group by year_released order by year_released;
#Q9
select language,avg(budget) from movies group by language having avg(budget)>50;
#Q10
select m.movie_title,d.company_name from movies m  join distribution_companies d on (m.distribution_company_id=d.id);