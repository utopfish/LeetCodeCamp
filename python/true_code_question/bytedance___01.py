# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:bytedance___01.py
#@time: 2020/8/18 23:02


n=int(input())
sts=[]
for _ in range(n):
    sts.append(list(input()))
for i in range(len(sts)):
    mark=0
    count=0
    while count!=len(sts[i])-1:
        if sts[i][count]==sts[i][count+1] and mark!=1:
            mark=1
            count+=1
            continue
        if mark!=0:
            if sts[i][count]==sts[i][count+1]:
                sts[i].pop(count)
                continue
            elif sts[i][count]!=sts[i][count+1] and sts[i][count]!=sts[i][count-1]:
                mark = 0
                continue
        count+=1


for st in sts:
    print("".join(st))