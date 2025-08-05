class Person:
    def __init__(self,fname,lname,age,prof,loc):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.proffesion=prof
        self.loc=loc
    def printt(self):
        print(self.fname,self.lname,self.age,self.proffesion,self.loc)
person1=Person('aswin','ms',19,'Python','Alappuzha')
person2=Person('ragav','s',25,'bigdata','Trissur')
person2.printt()
person1.printt()