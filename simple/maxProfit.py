# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:maxProfit.py
#@time: 2019/11/6 21:54
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro=0
        for i in range(1,len(prices)):
            temp=prices[i]-prices[i-1]
            if temp>0:pro+=temp
        return pro