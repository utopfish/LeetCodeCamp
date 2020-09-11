# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:tencent-4.py
#@time: 2020/9/6 21:11
num=int(input())
res=list(map(int,input().split()))
def getmed(data):
    data=sorted(data)
    size=len(data)
    median=data[(size-1)//2]
    return median
temp={}
for i in range(len(res)):
    temp[i]=res[i]
res = sorted(res)
for i in range(len(res)):
    target=temp.get(i)
    res.remove(target)
    median=getmed(res)
    print(median)
    res.insert(temp.get(i),target)