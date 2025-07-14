#Factorial of a number

def fact():
    mul=1
    num=int(input("Enter the number:"))
    for i in range(1,num+1):
        mul*=i
    print("Factorial1 is",mul)
fact()

def fact1(num):
    mul=1
    for i in range(1,num+1):
        mul*=i
    print("Factorial2 is",mul)
fact1(2)

def fact2(num):
    mul=1
    for i in range(1,num+1):
        mul*=i
    return mul
factorial=fact2(5)
print("factorial3 is",factorial)
factorial2=fact2(10)
print("factorial4 is",factorial2)