lst=[]
lst_even=[]
lst_odd=[]
for i in range(1,101):
    lst.append(i)
for i in lst:
    if i%2==0:
        lst_even.append(i)
    else:
        lst_odd.append(i)
print("list1:",lst)
print("even list1:",lst_even)
print("odd list1:",lst_odd)
print("sum of list1:",sum(lst))
print("sum of even list1:",sum(lst_even))
print("sum of odd list1:",sum(lst_odd))