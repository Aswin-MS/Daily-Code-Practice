""""2.You are given a list of integers, num_list, which represents a consecutive number series. In
this list:
There is one repeated number.
There is one missing number.
Your task is to write a Python function to:
• Identify the repeated number.
• Identify the missing number.
• Calculate the sum of the repeated and missing numbers.
Example 1:
num_list = [1, 1, 3, 4]
Output: 3 (Repeated number: 1, Missing number: 2, Sum: 1 + 2 = 3)
Example 2:
num_list = [1, 2, 2, 4]
Output: 5 (Repeated number: 2, Missing number: 3, Sum: 2 + 3 = 5)
Example 3:
num_list = [2, 3, 3, 5]
Output: 7 (Repeated number: 3, Missing number: 4, Sum: 3 + 4 = 7)"""
n=int(input())
num_list=[]
for i in range(0,n):
    num_list.append(int(input()))
for i in num_list:
    n1=i
    n2=i+1
    dif=n2-n1
    break
lst=[]
rn=0
mv=0
for i in range(num_list[0],num_list[n-1]+1):
    lst.append(i)
    i+=1
print(lst)
for i in num_list:
    for j in lst:
        print(i)
        print(j)
        break








    #     if i == j:
    #         break
    #     else:
    #         rn = i
    #         mv = j
    #         break
    # print(rn)
    # print(mv)
    # print('sum:', rn + mv)
