#lum
# lst1=[i for i in range(1,1001) if i%7==0]
# print(lst1)
# lst2=[i for i in range(1,1001) if i in  ]
# print(lst2)
string='Practice list comprehension problems to drill your head'
# lst3=[i for i in string if i==' ']
# print(len(lst3))
vow='aeiouAEIOU'
# lst4=[i for i in string if i in vow]
# print(len(lst4))
# lst5=[i for i in string if i not in vow and i!=' ']
# print(len(lst5))
lst1=[1,2,3,4]
lst2=[2,3,4,5]
# lst6=[i for i in lst1 if i in lst2]
# print(len(lst6))
string1='In 1984 there were 13 instances of a protest with over 1000 people attending'
n=10
print(type(n))
lst7=[i for i in string1 if type(i)=='int']
print(lst7)