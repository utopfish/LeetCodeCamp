#@Time:2020/9/18 20:31
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:meituan02.py
__author__ = "liuAmon"

"""
5
meituanapp
meituanwaimai
dianpingliren
dianpingjiehun
mt
"""

n=int(input())
sts=[]
for _ in range(n):
    sts.append(input())
max_len=max([len(i) for i in sts])
m=[{} for _ in range(max_len)]
for i in range(n):
    for index,j in enumerate(sts[i]):
        m[index][j]=m[index].get(j,0)+1
for i in range(n):
    for index,j in enumerate(sts[i]):
        if m[index][j]<2:
            print(sts[i][:index+1])
            break
        if index==len(sts[i])-1:
            print(sts[i])

