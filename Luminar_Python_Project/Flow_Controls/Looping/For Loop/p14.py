
l_limit=int(input("Enter the lower limit:"))
u_limit=int(input("Enter the upper limit:"))
sum1=0
sum2=0
for i in range(l_limit,u_limit+1):
    if i%2==0:
        sum1+=i
    else:
        sum2+=i
print("Sum of even numbers is",sum1)
print("Sum of odd numbers is",sum2)