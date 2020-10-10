#@Time:2020/9/3 16:28
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:o14cuttingRope.py
__author__ = "liuAmon"


def cuttingRope(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            tmp = max(j, dp[j]) * max(i - j, dp[i - j])
            dp[i] = max(dp[i], tmp)
    return dp[-1]


