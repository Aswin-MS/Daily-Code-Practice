"""
8. *Pop Until Even*

*Task:* Keep pop()-ing elements from the end until you find an even number. Print the even number.

*Example:*

python
lst = [3, 5, 7, 9, 10, 13]


"""
lst = [3, 5, 7, 9, 10, 13]
lst.reverse()

for i in lst:
    if i%2!=0:
        lst.pop(0)
    else:
        print("Even number:",i)
        break
