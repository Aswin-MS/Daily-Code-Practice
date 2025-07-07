
l_limit=int(input("Enter the lower limit:"))
u_limit=int(input("Enter the upper limit:"))

while l_limit<=u_limit:
    if l_limit%5==0:
        print(l_limit)
    l_limit+=1
