""" Question: Traffic Light Simulator
 Scenario: A traffic light cycles every 30 seconds (Red → Green → Yellow → Red…). Simulate it for
 N cycles.
 Sample Input:
 N = 2
 Sample Output:
 Cycle 1: Red, Green, Yellow Cycle 2: Red, Green, Yellow"""
def cycle(n):
    for i in range(1,n+1):
        print(f'Cycle {i}:Red,Green,Yellow',end=' ')
n=int(input())
cycle(n)