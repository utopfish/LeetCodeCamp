# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:ali_test02.py
#@time: 2020/8/28 19:16
import itertools
n,m=map(int,input().split(" "))
arr=list(str(n))
pailie = list(itertools.permutations(arr))
res={}
count=0
for x in pailie:
    temp=[]
    for y in x:
        temp.append(y)
    temp="".join(temp)
    if len(temp) ==len(str(int(temp))):
        if int(temp)%m==0 and temp not in res.keys():
            count+=1
            res[temp]=1
print(count)

