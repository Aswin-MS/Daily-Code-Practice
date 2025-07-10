#check given number is prime or not

num=int(input("Enter the number:"))

count=0
if (num==1)|(num==0):
    print("Not prime")

else:
    for i in range(2,num):
        if num%i==0:
            count+=1
    if count>=1:
        print("it is not a prime number ")
    else:
        print("It is a prime number")



"""
#OR
num=int(input("Enter the number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("it is a prime number ")
else:
    print("It is not a prime number")

#OR 
#we can set a flag, no need to increment the count
#so if the flag is greater than 0, it is not prime

num=int(input("Enter the number:"))
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
if flag>0:
    print("it is not a prime number ")
else:
    print("It is a prime number")
"""
