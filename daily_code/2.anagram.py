"""
2. Valid Anagram

Given two strings, check if they contain the same characters with the same frequencies.

"""
def ana(s1,s2):
        dic={}
        if len(s1)!=len(s2):
            return False
        for i in s1:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in s2:
            if i in dic:
                dic[i]-=1
            else:
                return False
            if dic[i]==0:
                del dic[i]
        if len(dic)==0:
            return True
        else:
            return False
#counter can be used from collections module
# from collections import Counter
# return Counter(s1)=Counter(s2)



s1=input()
s2=input()
ans=ana(s1,s2)
print(ans)