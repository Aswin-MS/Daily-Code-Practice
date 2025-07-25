"""
1. *Remove All Odd Numbers*

*Task:* From a given list of numbers, use a loop to remove all odd numbers using remove().

*Example:*

python
nums = [1, 2, 3, 4, 5, 6, 7]

"""
lst=[1,2,3,4,5,6,7]
for i in lst:
    if i%2!=0:
        lst.remove(i)
print(lst)