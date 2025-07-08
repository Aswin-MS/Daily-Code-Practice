#Factorial

num=int(input("Enter the number:"))

mul=1
for i in range(1,num+1):
    mul*=i

print(f"Factorial of {num} is {mul}")