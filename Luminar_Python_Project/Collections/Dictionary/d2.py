dic={'id':101,'fname':'vinay','lname':'k',
     'age':32,'prof':'python','salary':2500}
print(dic)
print(dic['age'])

###########
print("1st qn:")
for i in dic:
    print(i,':',dic[i])
#update value:
dic['id']=100
dic['salary']-=1000
print(dic)
#add new key value pair
dic['marks']=40
print(dic)
print('age' in dic)
print('dept' in dic)
print('prof' not in dic)
#delete key-value pair:
del dic['lname']
print(dic)
