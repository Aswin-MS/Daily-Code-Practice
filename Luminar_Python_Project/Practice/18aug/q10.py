""" Question: Harshad Number Checker
 Scenario: Check if a number is a Harshad number (divisible by the sum of its digits).
 Sample Input:
 Number: 18
 Sample Output:
 18 is a Harshad number"""

num=int(input())
summ=sum(int(i) for i in str(num))
if summ!=0:
    if num%summ==0:
        print(f"{num} is Harshad number.")
    else:
        print(f"{num} is not Harshad number.")

else:
    exit()