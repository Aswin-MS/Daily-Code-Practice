
l_limit=int(input("Enter the lower limit:"))
u_limit=int(input("Enter the upper limit:"))
summ=0
for i in range(l_limit,u_limit+1):
    if i%5==0:
        summ+=i

print("sum is", summ)

