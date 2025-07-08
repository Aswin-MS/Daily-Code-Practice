l_limit=int(input("Enter the lower limit:"))
u_limit=int(input("Enter the upper limit:"))

for i in range(l_limit,u_limit+1):
    if i%2==0:
        print(i)