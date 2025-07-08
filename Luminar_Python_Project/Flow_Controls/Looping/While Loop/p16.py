#Reverse a Number

num=int(input("Enter the number:"))
rev=0
while num!=0:
    n=num%10
    rev=rev*10+n
    num//=10
print("Reverse is",rev)

'''
OR
#Reverse a number 2
num=int(input("Enter the number:"))
rev=0
while num!=0:
    n=num%10
    rev=rev*10+n
    num=int((num-n)/10)
print(rev)
OR
#Reverse a number 2
num=int(input("Enter the number:"))
rev=0
print("Reverse is:")
while num!=0:
    n=num%10
    rev=n
    print(rev,end="")
    num//=10
'''
