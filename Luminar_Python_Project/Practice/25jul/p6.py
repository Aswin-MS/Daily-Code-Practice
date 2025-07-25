"""
6. *Check and Extend List*

*Task:* If a list has fewer than 5 elements, use extend() with a second list to make it 5 or more.

*Example:*

python
a = [1, 2]
b = [3, 4, 5]


"""
a = [1, 2]
b = [3, 4, 5]
if len(a)<5:
    a.extend(b)
print(a)
