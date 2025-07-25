"""
4. *Track Top 3 Scores*

*Task:* Ask the user to input 5 scores. Store only the top 3 scores in a list using append(), sort() and pop() if needed.

"""
lst=[]
for i in range(0,5):
    lst.append(int(input("enter the score:")))
lst.sort(reverse=True)
print("Top 3 scores:",lst[0:3])