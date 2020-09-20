# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:meituan_03.py
#@time: 2020/9/20 10:53
n,m=map(int,input().split())
t=input()
p=input()
i,j=0,0
res=0
while i<n and j<m:
    if t[i]==p[j]:
        res+=(i+1)
        i+=1
        j+=1
    else:
        i+=1
if j==len(p):
    print("YES")
    print(res)
else:
    print("NO")
