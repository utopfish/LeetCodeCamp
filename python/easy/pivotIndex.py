# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:pivotIndex.py
#@time: 2019/10/30 17:16
from typing import List
class Solution:
    '''
    超时
    '''
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==0:
            return -1
        else:
            for ind in range(len(nums)-1):
                if sum(nums[:ind])==sum(nums[ind+1:]):
                    return ind
            if sum(nums[1:]) == 0:
                return 0
            elif sum(nums[:-1]) == 0:
                return len(nums) - 1
            return -1
class Solution2:
    '''
    官方解答
    '''
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
if __name__=="__main__":
    Test=Solution()
    print(Test.pivotIndex([1,7,3,6,5,6]))