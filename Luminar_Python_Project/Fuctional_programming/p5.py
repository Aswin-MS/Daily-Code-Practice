dic={'bike':500,'cycle':50,'car':3000,'mini_bus':5000,'jeep':4500,'bus':8000}
lst=[i.upper() for i in dic if dic[i]>3000]
print(lst)