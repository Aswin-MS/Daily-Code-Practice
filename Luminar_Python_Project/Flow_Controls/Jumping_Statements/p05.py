l=int(input("Enter lower limit:"))
u=int(input("Enter upper limit:"))

for i in range(l,u+1):
    if i%2==0:
        continue
    print(i)