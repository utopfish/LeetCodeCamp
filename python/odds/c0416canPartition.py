# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0416canPartition.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/11 15:55
"""
"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

    每个数组中的元素不会超过 100
    数组的大小不会超过 200

示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].

 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

第一直觉是先使用sort，再进行分割。但是错的，使用背包来解决。使用boolean来设置dp表
之后好好看看<背包九讲>,当前方法还可以继续剪枝，并且使用一维表格记录dp
https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/
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



class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==0:return False
        sum_num=sum(nums)
        # 特判：如果是奇数，就不符合要求
        if sum_num&1==1:return False
        target=sum_num//2
        dp=[False]*(target+1)
        # 先填表格第 0 行，第 1 个数只能让容积为它自己的背包恰好装满
        if nums[0]<=target:
            dp[nums[0]]=True
        for i in range(1,n):
            for j in range(target,nums[i],-1):
                if dp[target]:return True
                dp[j]=dp[j] or dp[j-nums[i]]
        return dp[target]


if __name__=="__main__":
    nums= [1, 5, 11, 5]
    s=Solution2()
    print(s.canPartition(nums))