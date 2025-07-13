count=0
flag=0
compnum=50
while flag!=1:
    num=int(input("Enter a number:"))
    count += 1
    if (num<compnum):
        print("Your guess is low")
    elif (num>compnum):
        print("Your guess is high")
    else:
        count+=1
        flag=1
print("Well done, you took",count,"attempts")
