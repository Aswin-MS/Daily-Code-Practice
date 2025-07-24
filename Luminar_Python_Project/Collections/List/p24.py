#print lst1=[88,85,77,70,80,84,86,65,85]
lst=[2,5,13,20,10,6,4,25,5]
lst1=[]
summ=sum(lst)
for i in lst:
    lst1.append(summ-i)

print(f"lst1:{lst1}")
