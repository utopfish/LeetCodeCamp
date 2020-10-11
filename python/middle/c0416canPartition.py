# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0416canPartition.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/11 15:55
"""
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==0:return False
        sum_num=sum(nums)
        # 特判：如果是奇数，就不符合要求
        if sum_num&1==1:return False
        target=sum_num//2
        dp=[[False]*(target+1) for _ in range(n)]
        # 先填表格第 0 行，第 1 个数只能让容积为它自己的背包恰好装满
        if nums[0]<=target:
            dp[0][nums[0]]=True
        for i in range(1,n):
            for j in range(target+1):
                dp[i][j] = dp[i - 1][j]

                if nums[i] == j :
                    dp[i][j] = True
                    continue

                if (nums[i] < j) :
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        return dp[-1][target]


if __name__=="__main__":
    nums= [1, 5, 11, 5]
    s=Solution()
    print(s.canPartition(nums))