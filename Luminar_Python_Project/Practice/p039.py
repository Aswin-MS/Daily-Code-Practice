num=int(input("Enter the number whose multiplication table needed:"))
print("The multiplication table of",num,":")
mul=1
for i in range(1,13):
    mul=i*num
    print(f"{i}*{num}={mul}")