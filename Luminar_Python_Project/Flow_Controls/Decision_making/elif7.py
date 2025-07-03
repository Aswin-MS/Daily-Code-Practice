#Read 3 nos. from user, find the second-largest number

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))

if (num1>num2>num3)|(num3>num2>num1) :
    print("The second largest number is",num2)
elif (num2>num1>num3)|(num3>num1>num2):
    print("The second largest number is",num1)
elif (num1>num3>num2)|(num2>num3>num1):
    print("The second largest number is",num3)
else:
    print("ALL ARE EQUAL")


"""
OR
mylist=[num1,num2,num3]
mylist.sort()
print("The second largest number is",mylist[1])

OR
Using nested if:
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print('Number 2 is second largest')
    else:
        print('Number 3  is second largest')
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print('Number 1 is second largest')
    else:
        print('Number 3 is second largest')
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print('Number 1 is second largest')
    else:
        print('Number 2 is second largest')
else:
    print('All are equal')
"""