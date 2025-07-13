num=int(input("Enter the number:"))
summ=0
for i in range(1,num+1):
    if i==3:
        continue
    summ+=i
print("sum is",summ)