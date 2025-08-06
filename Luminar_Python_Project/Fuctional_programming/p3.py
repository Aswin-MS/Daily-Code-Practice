lst=[1,4,6,7,8,10,15,3,5]
lst1=[i+6 for i in lst]
print(lst1)
lst2=[i**2 for i in lst]
print(lst2)
lst3=[i for i in lst if i**2>36]
print(lst3)