"""
2. *Count Vowels in a List of Characters*

*Task:* Count how many vowels are in the list using a loop and count().

*Example:*

python
chars = ['a', 'b', 'e', 'i', 'o', 'u', 'k', 'm']


"""
chars = ['a', 'b', 'e', 'i', 'o', 'u', 'k', 'm']
vow=['a','e','i','o','u']
count=0
for i in chars:
    if i in vow:
        count+=1
print(count)