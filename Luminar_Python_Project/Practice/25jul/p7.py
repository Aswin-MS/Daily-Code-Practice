"""
7. *Count and Remove All Duplicates*

*Task:* Using a loop, remove all duplicates from a list and also print how many were removed.

*Example:*

python
data = ['a', 'b', 'a', 'c', 'b', 'd']

"""
data = ['a', 'b', 'a', 'c', 'b', 'd']
data1=[]
count=0
for i in data:
    if i not in data1:
        data1.append(i)
    else:
        count+=1
print("list without duplicates:",data1)
print("Number of items removed:",count)