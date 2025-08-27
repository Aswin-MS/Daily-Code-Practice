""" Question: Simple Spell Checker
 Scenario: A system flags words longer than 10 characters as 'suspicious'. Write a program that
 checks each word entered until the user types 'exit'.
Sample Input:
 Input words: programming, data, exit
 Sample Output:
 'programming' is suspicious"""

def check(inp):
    if len(inp)>10:
         print(f"'{inp}' is suspicious")
    else:
        pass
while True:
    inp=input()
    check(inp)
    if inp=='exit':
        exit()
