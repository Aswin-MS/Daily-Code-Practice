class student:
    def std(self,id,fname,lname,age,course,clg):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course
        self.clg=clg
    def printt(self):
        print(self.id,self.fname,self.lname,self.age,self.course,self.clg)
std1=student()
std1.std(1,'aswin','ms',22,'CS','AJCE')
std1.printt()
std2=student()
std2.std(2,'arjun','ms',20,'ME','MITS')
std2.printt()
std3=student()
std3.std(3,'vinay','k',22,'CS','SJCET')
std3.printt()
std4=student()
std4.std(4,'rahul','s',21,'ECE','CET')
std4.printt()
std5=student()
std5.std(5,'rehan','t',22,'CS','AJCE')
std5.printt()