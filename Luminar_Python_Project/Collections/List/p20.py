string='luminartechnolab'
count=0
count1=0
for i in string:
    if (i=='a')|(i=='e')|(i=='i')|(i=='o')|(i=='u'):
        count+=1
    else:
        count1+=1
print("Count of vowels:",count)
print("Count of consonants:",count1)

lst=[]
lst1=[]
vow='aeiouAEIOU'
for i in string:
    if i in vow:
        lst.append(i)
    else:
        lst1.append(i)
print("vowels:",lst)
print("Count of vowels:",len(lst))
print("consonants:",lst1)
print("Count of consonants:",len(lst1))


