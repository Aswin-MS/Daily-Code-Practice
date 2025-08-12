"""
Encryption question:

Create a program that takes a number as input (e.g., 2) and an alphabet letter (either uppercase or lowercase). The output should be the letter that is the given number of positions ahead of the input letter in the alphabet. For example, if the input is 2 and the letter is 'A', the output should be 'C'. Similarly, for lowercase letters, if the input is 2 and the letter is 'a', the output should be 'c'.
"""
num=int(input("enter a number:"))
alp=input("Enter the string:")
lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in lst:
    if alp==lst[i]:
        i=+2
        print(lst[i])


