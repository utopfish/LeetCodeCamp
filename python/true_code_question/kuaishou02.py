#@Time:2020/9/7 11:21
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:kuaishou02.py
__author__ = "liuAmon"

n=int(input())
nums=list(map(int,input().split()))
nums.sort()
dp=[[1]*(n) for _ in range(n)]
for i in range(1,n):
    if nums[i]-nums[i-1]==1:
        dp[i][0]=dp[i-1][0]+1
for i in range(1,n):
    for j in range(1,n):
        if i>j and nums[i]-nums[j]==i:
            dp[i][j]=dp[i][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])