"""
11. *Shift Elements Left (Rotate)*

*Task:* Rotate a list to the left by 1 using pop() and insert() in a loop.

*Example:*

python
data = [10, 20, 30, 40]
# Output should be [20, 30, 40, 10]

"""
#ANS:
data = [10, 20, 30, 40]
d1=data.pop(0)
data.insert(len(data),d1)
print(data)

