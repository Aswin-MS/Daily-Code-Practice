num=int(input("Enter how many people do you want to invite to the party:"))
if num<=10:
    for i in range(0,num):
        name=input("Enter the name:")
        print(f"{name} has been invited")
else:
    print("Too many people")

