# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5561.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/11/8 10:37
"""

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<1:
            return 0
        dp=[0]*(n+1)
        dp[1]=1
        if n<3:
            return 1
        for i in range(2,n+1):
            if i%2==0:
                dp[i] = dp[i // 2]
            else:
                dp[i]=dp[i//2]+dp[i//2+1]
        return max(dp)

if __name__=="__main__":
    n=7
    s=Solution()
    print(s.getMaximumGenerated(n))