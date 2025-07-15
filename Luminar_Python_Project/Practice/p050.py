flag=0
while flag!=1:
    num=int(input("Enter a number between 10 and 20:"))
    if num<10:
        print("Too low\nTry again!")
    elif num>20:
        print("Too high\nTry again!")
    else:
        flag=1
print("Thank You")