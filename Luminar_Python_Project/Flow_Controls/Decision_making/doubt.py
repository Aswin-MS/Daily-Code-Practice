#largest among 3 numbers

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1>num2&num1>num3:
    print('Number one is greater')
elif num2>num1&num2>num3:
    print('Number 2 is greater')
elif num3>num1 & num3>num2:
    print('Number 3 is greater')
else:
    print("all are equal")

"""
OR

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1<num2>num3:
    print("2")
elif num2<num1>num3:
    print("1")
else:
    print("3")
"""