# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:baidu_02.py
#@time: 2020/9/3 20:10
n=int(input())
nums=[]
if n==0:
    print(0)
for i in range(n):
	nums.append(list(map(int,input().split(" "))))

dp=[[0]*(n) for _ in range(n)]
dp2=[[0]*(n) for _ in range(n)]
for i in range(1,n):
    dp[i][0]=dp[i-1][0]+abs(nums[i][0]-nums[i-1][0])
    dp[0][i]=dp[0][i-1]+abs(nums[0][i]-nums[0][i-1])
for i in range(1,n):
    for j in range(1,n):
        dp[i][j]=min(dp[i-1][j]+abs(nums[i-1][j]-nums[i][j]),dp[i][j-1]+abs(nums[i][j-1]-nums[i][j]))

print(dp[-1][-1])
