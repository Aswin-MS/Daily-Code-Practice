#Method 3
#syntax:
#       var=[print if condition else print2 range]
#if  more than 2 conditions:
# var=[print if condition1 else print2 if condition2 else print3 range]
# lst=[i**2 if i%2==0 else i**3 for i in range(1,51) ]
# print(lst)
lst=['small' if i<=15 else 'medium' if i<=35 else 'large' for i in range(1,51)]
print(lst)