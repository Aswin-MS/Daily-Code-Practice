if __name__ == '__main__':
    lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
    print(lst)
    lst.sort()
#
# lst=[1,2,3,4]
# for i in range(len(lst)):
#     print(i)