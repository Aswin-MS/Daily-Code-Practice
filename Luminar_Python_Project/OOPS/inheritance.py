class A:
    def printa(self,num1):
        self.num1=num1
        print('Inside class A is',self.num1)
class B(A):
    def printb(self,num2):
        self.num2=num2
        print('Inside class B is',self.num2)
obj1=B()
obj1.printb(5)
obj1.printa(10)