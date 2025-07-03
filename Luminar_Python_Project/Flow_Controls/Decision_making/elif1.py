#check given number is positive or negative

num=int(input("Enter the number:"))

if num<0:
    print("The number is Negative!")
elif num==0:
    print("The number is neither positive nor negative!")
else:
    print("The number is Positive!")