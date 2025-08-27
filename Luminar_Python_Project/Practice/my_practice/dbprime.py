
u_limit=int(input("Enter the upper limit:"))
u=u_limit
lst=[]
count=0
for i in range(1,u+1):
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        lst.append(i)
        count=0
    else:
        count=0
print(len(lst))