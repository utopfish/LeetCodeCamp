#@Time:2020/9/19 15:12
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:bytedance_02.py
__author__ = "liuAmon"

n,m,c=map(int,input().split())
color=[]
for _ in range(n):
    color.append(list(map(int,input().split()))[1:])

hash={}
count=0
for i in range(1,c+1):
    for j in range(n):
        if i in color[j]:
            hash[i]=hash.get(i,[])+[j]
res=0
for h in hash.keys():
    if len(hash[h])>1:
        count=0
        tmp = sorted(hash[h])
        for i in range(1,len(tmp)):
            if abs(hash[h][i-1]-hash[h][i])< m:
                count+=1
        if hash[h][0]==0 and hash[h][-1]==n-1:
            count+=1
        if count!=0:
            res+=1
print(res)

