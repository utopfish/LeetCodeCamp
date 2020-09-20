#@Time:2020/9/18 20:07
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:meituan01.py
__author__ = "liuAmon"
"""
4
3 2 4 1

4
78 58 62 64

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
