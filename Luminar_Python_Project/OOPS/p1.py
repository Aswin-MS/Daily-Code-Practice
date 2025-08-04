class Person:
    def value(self,fname,lname,age,prof,loc):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.proffesion=prof
        self.loc=loc
    def printt(self):
        print(self.fname,self.lname,self.age,self.proffesion,self.loc)
person1=Person()
person1.value('aswin','ms','22','unemployed','wayanad')
person1.printt()
