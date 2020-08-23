#@Time:2020/8/19 19:41
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:test.py
__author__ = "liuAmon"


n,m=map(int,input().strip().split(" "))
num=list(map(int,input().strip().split(" ")))
di={}
for i in num:
    if i in di.keys():
         di[i]+=1
    else:
         di[i]=1
res=[]
for  i in num:
    if di[i]<=m:
         res.append(str(i))
print(" ".join(res))
