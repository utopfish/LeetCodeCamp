#@Time:2020/9/18 22:50
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:money.py
__author__ = "liuAmon"
"动态规划，纸币分配"
n=int(input())
money = [1,5,10,20,50,100]
dp = [0 for i in range(n+1)] # dp[i]指n为i时的拼凑方法数
dp[0] = 1 #当n为0是，方法数为1
for item in money:
    for i in range(1,n+1):
        if i >= item:
            dp[i] += dp[i-item]
print(dp[n])