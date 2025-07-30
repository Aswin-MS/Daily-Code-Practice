f=open('C:/Users/user/Downloads/sample4.txt','r')
#1st qn
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if age>'22':
#         print(data)
#2nd qn
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if age=='23':
#         print(data[1:5])
#3rd qn
# for i in f:
#     data=i.rstrip('\n').split(',')
#     work=data[5]
#     if work=='Chennai':
#
#         print(data[1:4])
#4th qn:
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[3]
    work=data[5]
    if (age>'23') & (work=='Chennai'):
        print(data[1:6:2])