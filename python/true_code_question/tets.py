# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:tets.py
#@time: 2020/9/6 19:52
n=int(input())
s1=list(map(int,input().split()))
m=int(input())
s2=list(map(int,input().split()))
len1=len(s1)
len2=len(s2)
i,j=0,0
res=[]
while i<len1 and  j<len2:
    if s1[i]==s2[j]:
        res.append(str(s1[i]))
        i+=1
        j+=1
        continue
    elif s1[i]>s2[j]:
        i+=1
        continue
    else:
        j+=1
        continue
print(" ".join(res))