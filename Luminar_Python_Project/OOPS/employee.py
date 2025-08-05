class Person:
    def per(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
class Employee(Person):
    def emp(self,prof,exp,salary,loc):
        self.prof=prof
        self.exp=exp
        self.salary=salary
        self.loc=loc
        print('Details:',self.fname,self.lname,self.age,self.prof,self.exp,self.salary,self.loc)

emp1=Employee()
emp1.per('aswin','ms',22)
emp1.emp('bigdata','2 years',15000,'Bangalore')

emp2=Employee()
emp2.per('rehan','v',25)
emp2.emp('sql','5 years',10000,'Mysuru')