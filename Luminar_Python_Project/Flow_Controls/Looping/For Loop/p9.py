#Multiplication Table

num=int(input("Enter the number:"))
mul=1
for i in range(1,11):
    mul=i*num
    print(i,"*",num,"=",mul)