def add():
    l=int(input("Enter Lower limit:"))
    u=int(input("Enter Upper limit:"))
    sum1=0
    sum2=0
    for i in range(l,u+1):
        if i%2==0:
            sum1+=i
        else:
            sum2+=i
    print("The sum of even numbers is",sum1)
    print("The sum of odd numbers is", sum2)
add()