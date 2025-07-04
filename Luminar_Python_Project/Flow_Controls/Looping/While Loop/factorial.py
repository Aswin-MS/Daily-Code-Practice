 #FACTORIAL

num=int(input("Enter the number:"))
i=1
mul=1

while i<=num:
    mul*=i
    i+=1
print("factorial is",mul)