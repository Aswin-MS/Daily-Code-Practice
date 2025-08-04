class Employee:
    dept='SDE'
    comp='TCS'
    def emp(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
    def printt(self):
        print(self.id,self.fname,self.lname,self.age,Employee.dept,Employee.comp)
emp1=Employee()
emp1.emp(101,'regha','k',26)
emp1.printt()
emp2=Employee()
emp2.emp(102,'megha','t',28)
emp2.printt()
emp3=Employee()
emp3.emp(103,'sneha','r',22)
emp3.printt()