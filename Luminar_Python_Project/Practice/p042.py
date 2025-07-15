total=0
for i in range(0,5):
    num=int(input("Enter the number:"))
    ans=input("Do you want to add this to the total(y/n):")
    if ans=='y':
        total+=num
    elif ans=='n':
        continue
    else:
        print("Invalid input")
print("The total is",total)