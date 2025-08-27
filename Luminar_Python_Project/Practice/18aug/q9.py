""" Question: LCM of Two Numbers
 Scenario: Compute the Least Common Multiple (LCM) of two numbers.
 Sample Input:
 Numbers: 12, 18
 Sample Output:
 LCM: 36"""
def gcd(a,b):
    while b:
        a,b=b,a%b
    return abs(a)
def lcm(a,b):
    if a==0 or b==0:
        return 0
    return abs(a*b)//gcd(a,b)
a=int(input())
b=int(input())
print(lcm(a,b))