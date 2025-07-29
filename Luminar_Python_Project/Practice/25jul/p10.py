"""10. *Combine and Remove Specific Items*

*Task:* Combine two lists using extend() and then remove all occurrences of a specific word.

*Example:*

python
list1 = ["pen", "pencil", "eraser"]
list2 = ["scale", "pencil", "pen"]
"""
#ANS:
list1 = ["pen", "pencil", "eraser"]
list2 = ["scale", "pencil", "pen"]
list1.extend(list2)
word=input("Enter the word to be removed:")
for i in list1:
    if i==word:
        list1.remove(i)
print(list1)