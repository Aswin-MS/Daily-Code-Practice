total=0

while total<=50:
    num=int(input("Enter a number to be added:"))
    total+=num
    if total<=50:
        print("The total is", total)
    else:
        print("Total over 50, program terminated")

