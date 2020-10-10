#@Time:2020/9/18 22:33
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:stoneLine.py
__author__ = "liuAmon"
"""
4
3 2 4 1

4
78 58 62 64

石子合并，动态规划
https://blog.csdn.net/weixin_43939593/article/details/105406704
"""

length = int(input())
coins = list(map(int, input().split()))
dp = [[float("inf")] * length for _ in range(length)]
for i in range(length - 1, -1, -1):
    for j in range(i, length):
        if i == j:
            dp[i][j] = 0
        else:
            curSum = sum(coins[i: j + 1])
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + curSum)

print(dp[0][-1])