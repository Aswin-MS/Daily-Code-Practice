flag=0
num=0
while flag!=1:
    if num<=5:
        num = int(input("Enter a number:"))
    else:
        print("The last number you have entered was",num)
        flag=1