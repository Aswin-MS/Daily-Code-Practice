l_limit=int(input("Enter the lower limit:"))
u_limit=int(input("Enter the upper limit:"))

summ1=0
summ2=0
while l_limit<=u_limit:
    if l_limit%2==0:
        summ1+=l_limit
    else:
        summ2+=l_limit
    l_limit+=1
print("Sum of even numbers is", summ1)
print("Sum of odd numbers is", summ2)