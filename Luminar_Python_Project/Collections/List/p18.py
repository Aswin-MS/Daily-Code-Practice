#Duplicate values count
lst=[1,30,20,30,40,50,40,30,20,10,10,10,20]
lst1=[]
count=0
for i in lst:
    if i not in lst1:
        lst1.append(i)
    elif i in lst1:
        count+=1

print(count)
