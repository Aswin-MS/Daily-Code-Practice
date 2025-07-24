lst=[1,5,2,4,7,8,11,12,13,20]
elem=int(input("Enter the number:"))
for i in lst:
    for j in lst:
        if i+j==elem:
            print(f'({i},{j})')