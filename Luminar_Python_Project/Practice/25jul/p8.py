"""
8. *Pop Until Even*

*Task:* Keep pop()-ing elements from the end until you find an even number. Print the even number.

*Example:*

python
lst = [3, 5, 7, 9, 10, 13]


"""
#ANS:
lst = [3, 5, 7, 9, 10, 13]
lst1=lst
lst.reverse()
for i in lst:
    if i%2!=0:
        lst1.pop()
    else:
        print(i)
        break

"""
OR
lst = [3, 5, 7, 9, 10, 13]

for num in reversed(lst):
    if num % 2 == 0:
        print("Found even number:", num)
        break
    else:
        lst.pop()

OR
lst = [3, 5, 7, 9, 10, 13]

while lst:
    num = lst.pop()
    if num % 2 == 0:
        print("Found even number:", num)
        break

"""