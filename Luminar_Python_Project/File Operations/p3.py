f=open('sample1','r')
lst=[]
for i in f:
    lst.append(int(i.rstrip('\n')))
print(lst)
print('sum:',sum(lst))