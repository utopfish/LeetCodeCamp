# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP019minimumOperations.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/10 10:19
"""
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n=len(leaves)
        dp=[[0,0,0] for _ in range(n)]
        dp[0][0]=int(leaves[0]=='y')
        dp[0][1]=dp[0][2]=dp[1][2] =float('inf')
        for i in range(1,n):
            isRed=int(leaves[i]=='r')
            isYellow=int(leaves[i]=='y')
            dp[i][0]=dp[i-1][0]+isYellow
            dp[i][1]=min(dp[i-1][0],dp[i-1][1])+isRed
            if i>=2:
                dp[i][2]=min(dp[i-1][1],dp[i-1][2])+isYellow
        return dp[-1][2]

#减小dp空间
class Solution2:
    def minimumOperations(self, leaves: str) -> int:
        n=len(leaves)
        a,b,c=int(leaves[0]=='y'),float('inf'),float('inf')
        for i in range(1,n):
            isRed=int(leaves[i]=='r')
            isYellow=int(leaves[i]=='y')
            if i<2:
                a ,b,c= a + isYellow,min(a, b) + isRed,b
            else:
                a, b, c =a + isYellow,min(a, b) + isRed,min(b,c)+isYellow
        return c

if __name__=="__main__":
    leaves = "rrryyyrryyyrr"
    s=Solution2()
    print(s.minimumOperations(leaves))