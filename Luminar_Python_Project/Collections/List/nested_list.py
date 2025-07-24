employee=[[101,'vinay','k',28,'python',1500],
          [102,'vipin','p',30,'bigdata',1750],
          [103,'anu','r',31,'python',1250],
          [104,'amal','r',32,'bigdata',1500],
          [105,'vimal','w',31,'python',1800]]
for i in employee:
    if i[3]>29:
        print(i)
print("2nd question:")
for i in employee:
    if i[3]==30:
        print(i[1:5])

print("3rd qn:")
for i in employee:
    if i[4]=='bigdata':
        print(i[1:4])
print("4th qn")
for i in employee:
    if i[4]=='python':
        print(i[1::2])

print("5th qn:")
for i in employee:
    if (i[3]>30) &(i[4]=='bigdata'):
        print(i[1:])
print("6th qn:")
summ=0
for i in employee:
    summ+=i[-1]

print(summ)