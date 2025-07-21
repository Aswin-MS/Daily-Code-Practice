#Count of consonanats:
string='luminartechnolab'
vow='aeiouAEIOU'
lst=[]
for i in string:
    if i not in vow:
        lst.append(i)
print("Consonants:",lst)
print("Count:",len(lst))