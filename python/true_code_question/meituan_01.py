# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:meituan_01.py
#@time: 2020/9/20 10:08
m,n=map(int,input().split())
res=0
for i in range(m,n+1):
    temp=str(i)
    if len(set(list(temp)))!=6:
        continue
    AB=temp[:2]
    CD=temp[2:4]
    EF=temp[4:]
    if AB[0]=='0':
        continue
    if int(AB)+int(CD)==int(EF):
        res+=1
print(res)