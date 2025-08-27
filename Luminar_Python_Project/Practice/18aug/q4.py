""" Question: Simple Alarm Clock
 Scenario: An alarm rings every 5 minutes from a given start time for N times.
 Sample Input:
 Start Time: 08:00, N = 3
 Sample Output:
 08:00, 08:05, 08:10"""
def alarm(stime,n):
    al=[]
    al=stime.split(':')
    t = int(al[1])
    for i in range(0,n):
        t+=5
        print(f'{al[0]}:{t:02d}',end=',')
stime=input()
n=int(input())
alarm(stime,n)