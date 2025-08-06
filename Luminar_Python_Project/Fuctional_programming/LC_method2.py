# Method 2
# syntax:
#         var=[print range if condition]
#eg:
# lst=[i for i in range(1,21) if i%2==0]
# print(lst)
# lst=[i for i in range(1,31) if i%2==1]
# print(lst)
# lst=[i**2 for i in range(1,21) if i%2==0]
# print(lst)
lst=[(i,i**3) for i in range(10,51) if i%5==0]
print(lst)