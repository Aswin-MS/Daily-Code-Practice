num=int(input("Enter the limit:"))
summ=0
for i in range(1,num+1):
    if i==6:
        break
    summ+=i
print("sum is",summ)