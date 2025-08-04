#temper
#Find the max. temperature of each district
f=open('D:/Aswin/Data Science/Daily-Code-Practice/temper','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    dis=data[0]
    temp=data[1]
    if dis not in dic:
        dic[dis]=temp
    else:
        old=dic[dis]
        if temp>old:
            dic[dis]=temp
for k,v in dic.items():
    print(k,":",v)