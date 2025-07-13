num1=int(input("Enter first no.:"))
num2=int(input("Enter second no.:"))
sum1=num1+num2
flag=0
while flag!=1:
    ans=input("Do you want to another number(y/n):")
    if ans=='y':
        num3=int(input("Enter the next number:"))
        sum1+=num3
    else:
        flag=1
print("The total sum is", sum1)