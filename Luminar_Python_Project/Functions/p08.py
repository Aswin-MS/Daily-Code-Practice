#create a simple calculator
def add(num1,num2):
    sum1=num1+num2
    print("The sum is",sum1)
def sub(num1,num2):
    sub1=num1-num2
    print("The difference is",sub1)
def mul(num1,num2):
    mul1=num1*num2
    print("The product is",mul1)
def div(num1,num2):
    div1=num1/num2
    print("The division is",div1)

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
choice=int(input("Enter your choice:"))
if choice==1:
    add(num1,num2)
elif choice==2:
    sub(num1,num2)
elif choice==3:
    mul(num1,num2)
elif choice==4:
    div(num1, num2)
else:
    print("Wrong choice")

