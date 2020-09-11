# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:tencet-2.py
#@time: 2020/9/6 20:20
n,m=map(int,input().split())
nums=[]
for i in range(m):
    temp = {}
    for j in list(map(int,input().split()))[1:]:
        temp[j]=j
    nums.append(temp)
queue=[0]
res={}
res[0]=0
while queue:
    temp=queue.pop(0)
    for i in range(m):
        if temp in nums[i].keys():
            for j in nums[i].keys():
                if j not in res.keys():
                    res[j]=j
                    queue.append(j)
print(len(res))