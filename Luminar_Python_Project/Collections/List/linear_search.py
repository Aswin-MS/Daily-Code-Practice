lst=[1,10,5,6,7,2,15,25,20,50,45,22]
num=int(input("Enter the element:"))
flag=0
for i in lst:
    if i==num:
        print("Element Found")
        flag=1
        break

if flag!=1:
    print("Not found")