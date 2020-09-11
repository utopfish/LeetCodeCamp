#@Time:2020/9/8 19:01
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:xiaomi01.py
__author__ = "liuAmon"
"""
2 3 2
1 2 3
1 2 3
1 1
1 1
1 1
"""


M,K,N=map(int,input().split())
a=[]
b=[]
for _ in range(M):
    a.append(list(map(int,input().split())))
for _ in range(K):
    b.append(list(map(int,input().split())))
res=[]
for i in range(M):
    temp=[]
    for j in range(N):
        sum=0
        for k in range(K):
            sum+=a[i][k]*b[k][j]
        temp.append(sum)
    res.append(temp)
print(res)

