# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:containsDuplicate.py
#@time: 2019/11/7 10:21
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if  len(nums)==0:return False
        res={}
        for ind,i in enumerate(nums):
            if i not in res:
                res[ind]=i
            else:
                return True
        return False
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
if __name__=="__main__":
    Test=Solution()
    print(Test.containsDuplicate([]))