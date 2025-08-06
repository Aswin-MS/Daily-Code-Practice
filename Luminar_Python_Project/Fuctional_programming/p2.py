string='luminartechnolab'
vow='aeiouAEIOU'
lst=[i for i in string if i in vow]
print(len(lst))
lst1=[i for i in string if i not in vow]
print(len(lst1))