# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:test.py
#@time: 2020/9/3 19:48
a=input().split(" ")
n=int(a[0])
m=int(a[1])
k=int(a[2])
nums=[]
for i in range(n):
    nums.append(input().split(" "))

dp=[[0]*(m+1) for _ in range(n+1)]
weight=[[[]]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=dp[i-1][j]
        weight[i][j]=weight[i][j]
        if j>=int(nums[i-1][1]) and dp[i][j]<dp[i-1][j-int(nums[i-1][1])]+int(nums[i-1][0]):
            dp[i][j]=dp[i-1][j-int(nums[i-1][1])]+int(nums[i-1][0])
            weight[i][j].append(int(nums[i-1][1]))
            weight[i][j].pop(j)


print(dp[-1][-1])

