#@Time:2019/11/16 10:23
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:maxProfit.py
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = max_profit = 0
        for i in range(len(prices)-1):
            temp = max(0, prices[i+1]-prices[i]+temp)
            max_profit = max(max_profit, temp)
        return max_profit

if __name__=="__main__":
    Test=Solution()
    print(Test.maxProfit([7,1,5,3,6,4]))