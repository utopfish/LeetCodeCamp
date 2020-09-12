# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:wangyi03.py
#@time: 2020/9/12 15:22
"""
输入:
amabc
输出：
3
(ama,长度为3)
"""

s=input()
n=len(s)
dp=[[0]*(n) for _ in range(n)]
def isgood(ts):
    temp={}
    for t in ts:
        if t in ['a','b','c','x','y','z']:
            temp[t]=temp.get(t,0)+1
    for i in temp.keys():
        if temp[i]%2==1:
            return False
    return True
for j in range(1,n):
    if isgood(s[:j]):
        dp[0][j]=j
    else:
        dp[0][j]=dp[0][j-1]
for i in range(1,n):
    for j in range(i+1,n):
        if not isgood(s[i:j]):
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        else:
            dp[i][j]=max(j-i,dp[i-1][j])
print(dp[-2][-1])

