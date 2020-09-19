#@Time:2020/9/19 19:12
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:bytedance05.py
__author__ = "liuAmon"

"""
4
0 2 6 5
2 0 4 4
6 4 0 2
5 4 2 0
输出：
13
动态规划旅行商问题
4
0 10 15 100
10 0 35 25
15 35 0 30
100 25 30 0
"""
import sys
n=int(input())
road=[]
for _ in range(n):
    road.append(list(map(int,input().split())))
v=1<<(n-1)
dp=[[float('inf')]*v for _ in range(n+1)]
for i in range(n):
    dp[i][0]=road[i][0]

for j in range(1,v):
    for i in range(n):
        if i!=0 and (((j >> (i - 1)) & 1) == 1):
            continue
        for k in range(1,n):
            if ((j>>(k-1))&1)==1:
                t=j^(1 << (k - 1))
                dp[i][j]=min(dp[i][j],road[i][k]+dp[k][j^(1 << (k - 1))])
print(dp[0][-1])