"""1. Contains Duplicate

Given an array, return true if any value appears more than once.

"""
def dup(arr):
    seen=set()
    for i in arr:
        if i not in seen:
            seen.add(i)
        else:
            return True
    return False
n=int(input())
arr=[int(input()) for _ in range(n)]
ans=dup(arr)
print(ans)
