
l_limit=int(input("Enter the lower limit:"))
u_limit=int(input("Enter the upper limit:"))

summ=0
while l_limit<=u_limit:
    if l_limit%2==1:
        summ+=l_limit
    l_limit+=1
print(summ)
