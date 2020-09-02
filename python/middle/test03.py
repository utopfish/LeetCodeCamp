#@Time:2020/9/2 20:24
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:test03.py
__author__ = "liuAmon"

import sys

if __name__ == "__main__":
    # 读取第一行的n
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    size = list(map(int, line.split()))

    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,k+1):
            if j<size[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-size[i-1]]+values[i-1])

    print(dp[n][k])