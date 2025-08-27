"""Question: Perfect Number Checker
 Scenario: Check if a number is perfect (sum of proper divisors equals the number).
 Sample Input:
 Number: 28
 Sample Output:
 28 is a perfect number"""
def prop(num):
    lst=[]
    for i in range(1,(num//2+1)):
        # print(i)
        if num%i==0:
            lst.append(i)
    if sum(lst)==num:
        print(f'{num} is a perfect number')
    else:
        pass
num=int(input())
prop(num)
