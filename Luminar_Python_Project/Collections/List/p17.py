lst=[9,0,9,1,4,3,6,8,4,6,9,3]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)

print(lst1)
print(len(lst1))
"""
OR
lst1=list(set(lst))
print(lst1)
"""