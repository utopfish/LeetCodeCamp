# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:tecent-5.py
#@time: 2020/9/6 21:43
from heapq import *
def addNum(res):
    A,B=[],[]
    for num in res:
        if len(A)!=len(B):
            heappush(B,-heappushpop(A,num))
        else:
            heappush(A,-heappushpop(B,-num))
    return A[0],-B[0]
num=int(input())
res=list(map(int,input().split()))
m,n=addNum(res)
for i in range(num):
    if res[i]>=m:
        print(n)
    elif res[i]<=n:
        print(m)