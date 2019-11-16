# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:maxProfit2.py
#@time: 2019/11/6 21:54
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        diff = [0 for _ in range(len(prices)-1)]
        for i in range(len(prices)-1):
            diff[i] = prices[i+1]-prices[i]
        dp = [0 for _ in range(len(prices)-1)]
        dp[0] = max(0, diff[0])
        max_profit = dp[0]
        for i in range(1, len(prices)-1):
            dp[i] = max(0, diff[i]+dp[i-1])
            max_profit = max(max_profit, dp[i])
        return max_profit

if __name__=="__main__":
    Test=Solution()
    print(Test.maxProfit([7,1,5,3,6,4]))