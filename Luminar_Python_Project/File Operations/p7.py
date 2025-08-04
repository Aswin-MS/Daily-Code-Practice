#Movie
"""
#1. year above 2000 name,year,rating,duration

#2. 1975 name,rating,duration

#3. 1975-2000 release name,year,rating

#4. Release year above 2000 and rating above 4 name,year,rating

#5. Rating below 3.5 movies name,rating,year

#6. Each year release movie count
"""
f=open('D:/Aswin/Data Science/Daily-Code-Practice\movies_cleaned_pandas.csv','r')
#Q1:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     yr=d[2]
#     if yr>'2000':
#         print(d[1:5])
#Q2:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     yr=d[2]
#     if yr=='1975':
#         print(d[1],d[3],d[4])
#Q3:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     yr=d[2]
#     if '1975'<=yr<='2000':
#         print(d[1:4])
#Q4:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     yr=d[2]
#     rat=d[3]
#     if yr>'2000' and rat>'4.0':
#         print(d[1:4])
#Q5:
# for i in f:
#     d=i.rstrip('\n').split(',')
#     rat=d[3]
#     if rat<'3.5':
#         print(f'{d[1]},{d[3]},{d[2]}')
#Q6:
# dic={}
# for i in f:
#     d=i.rstrip('\n').split(',')
#     yr=d[2]
#     if yr not in dic:
#         dic[yr]=1
#     else:
#         dic[yr]+=1
# for k,v in dic.items():
#     print(k,":",v)
