count=0
flag=0
while flag!=1:
    inv = input("Enter the name of the person to be invited:")
    count+=1
    ans=input("Do you want to invite somebody else(y/n):")
    if ans=='y':
        flag=0
    else:
        flag=1
print("The total count of guests are",count)
