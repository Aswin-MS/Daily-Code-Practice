lst=[1,3,5,4,2,0,5,7,8,9,12,10,8,7,6,8,12,13,11,8,5]
#generate lst1=[1,5,0,12,6,13]
lst1=[]
for i in range(0,len(lst)-1):
    if(lst[i-1]<lst[i]>lst[i+1]) or (lst[i-1]>lst[i]<lst[i+1]):
        lst1.append(lst[i])

print(lst1)