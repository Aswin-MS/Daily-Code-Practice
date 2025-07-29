"""### 🔹 9. *Reverse Word Order*

*Task:* Given a list of words, use reverse() and join them into a sentence.

*Example:*

python
words = ["world", "the", "to", "Welcome"]
"""
#ANS:
def reverse():
    words = ["world", "the", "to", "Welcome"]
    words.reverse()
    for i in words:
        print(i,end=' ')
    sent=' '.join(words)
    print(sent)

reverse()