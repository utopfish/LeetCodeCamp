"""
@author: liuAmon
@contact:utopfish@163.com
@file: LCP6207.py
@time: 2022/10/16 10:58
"""
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        i,j = 0,1
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if min(nums[i:j])==minK and max(nums[i:j])==maxK:
                    count+=1
                if min(nums[i:j])<minK or max(nums[i:j])>maxK:
                    continue
        return count