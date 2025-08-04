#Customer1
"""
#1. Age above 50 fname,lname,age,prof

#2. Age 25 to 40 fname,age,loc

#3. india work fname,lname,age,prof

#4. india and age above 50 fname,lname,age

#5. Doctor prof work fname,lname,age,prof

#6. uk work fname,lname,age,prof

#7. us and age below 30 fname,lname,age,prof

#8. india and prof Doctor fname,lname,age,prof

#9. Each prof count

#10. Each location count
"""
f=open('D:/Aswin/Data Science/Daily-Code-Practice/customer1.txt','r')
#Q1:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     if d[3]>'50':
#         print(d[1:5])
#Q2:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     if '25'<=d[3]<='50':
#         print(d[1:6:2])
#Q3:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     if d[-1]>'india':
#         print(d[1:5])
#Q4:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     place=d[-1]
#     if (d[3]>'50') & (place=='india'):
#         print(d[1:4])
#Q5:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     prof=d[4]
#     if prof=='Doctor':
#         print(d[1:5])
# Q6:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     place = d[-1]
#     if place=='uk':
#         print(d[1:5])
#Q7:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     place = d[-1]
#     age=d[3]
#     if (place=='us') & (age<'30'):
#         print(d[1:5])
#Q8:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     place = d[-1]
#     prof=d[-2]
#     if (place=='india') & (prof=='Doctor'):
#         print(d[1:5])
#Q9:
# dic={}
# for i in f:
#     d=i.rstrip('\n').split(',')
#     prof=d[4]
#     if prof not in dic:
#         dic[prof]=1
#     else:
#         dic[prof]+=1
# print(dic)
#Q10:
dic={}
for i in f:
    d=i.rstrip('\n').split(',')
    loc=d[-1]
    if loc not in dic:
        dic[loc]=1
    else:
        dic[loc]+=1
for i in dic:
    print(f'{i}:{dic[i]}')