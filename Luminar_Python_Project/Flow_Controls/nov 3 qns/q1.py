"""1 . Given an integer array nums of size n, return the number with the value closest to 0 in nums.
If there are multiple answers, return the number with the largest value.
Example 1:
Input: nums = [-4,-2,1,4,8]
Output: 1
Thus, the closest number to 0 in the array is 1.
Example 2:
Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned. """
from numpy.ma.core import append

n=int(input('enter no.'))
lst=[]
diff1=100
for i in range(0,n):
    lst.append(int(input()))
for i in lst:
    diff=abs(0-i)
    if diff<=diff1:
        diff1=diff
        ans=i
    else:
        continue

print(ans)
