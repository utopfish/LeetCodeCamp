# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:tencent-3.py
#@time: 2020/9/6 20:35
n,k=map(int,input().split())
nums=[]
res={}
for i in range(n):
    temp=input()
    if temp in res.keys():
        res[temp]+=1
    else:
        res[temp]=1
res=[tuple(i) for i in res.items()]
res.sort()
for i in range(k):
    print(str(res[i][0])+" "+str(res[i][1]))
def swap(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i][1]> arr[j][1]:
                arr[i],arr[j]=arr[j],arr[i]
            elif arr[i][1]==arr[j][1] and arr[i][0]>arr[j][0]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
res=sorted(res,key=lambda x:(x[1],x[0]))
for i in range(k):
    print(str(res[i][0])+" "+str(res[i][1]))