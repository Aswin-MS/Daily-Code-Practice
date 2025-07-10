l_limit=int(input("Enter the lower limit:"))
u_limit=int(input("Enter the upper limit:"))
l=l_limit
u=u_limit
count=0
for i in range(l,u+1):
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,end=",")
        count=0
    else:
        count=0