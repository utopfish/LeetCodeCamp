#@Time:2020/9/2 19:51
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:test02.py
__author__ = "liuAmon"

import sys
if __name__ == "__main__":
    # 读取第一行的n
    a = sys.stdin.readline().strip().split(",")
    n,m=int(a[0]),int(a[1])
    maps=[]
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        maps.append(line)
    dp=[[0]*m for _ in range(n)]

    for i in range(1,n):
        for j in range(1,m):
            if  maps[i][j]!=maps[i-1][j] and maps[i][j]!=maps[i][j-1]:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    print(dp[-1][-1]+1)