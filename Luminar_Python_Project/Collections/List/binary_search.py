lst=[1,10,5,2,15,30,18,12,7,3,14]
elem=int(input("Enter the element:"))
lst.sort()
flag=0
low=0
upper=len(lst)-1
while low<=upper:
    mid=(low+upper)//2
    if elem>lst[mid]:
        low=mid+1
    elif elem<lst[mid]:
        upper=mid-1
    elif elem==lst[mid]:
        print("element found")
        break
if flag!=1:
    print("element not found")