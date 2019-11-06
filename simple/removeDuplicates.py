# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:removeDuplicates.py
#@time: 2019/11/6 21:42
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return list(set(nums))
class Solution2:
    '''
    倒序遍历
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        for num_index in range(len(nums)-1, 0, -1):
            if nums[num_index] == nums[num_index-1]:
                nums.pop(num_index)
        return len(nums)
if __name__=="__main__":
    Test=Solution()
    print(Test.removeDuplicates([1,2,3,3]))