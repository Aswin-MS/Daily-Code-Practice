dire=input("Which direction do you want to count(up/down):")
if dire=='up':
    num=int(input("enter the upper limit:"))
    for i in range(1,num+1):
        print(i,end=' ')
elif dire=='down':
    num=int(input("Enter a number below 20:"))
    for i in range(20,num-1,-1):
        print(i,end=' ')
else:
    print("I don't understand")