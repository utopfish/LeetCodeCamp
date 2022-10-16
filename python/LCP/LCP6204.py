"""
@author: liuAmon
@contact:utopfish@163.com
@file: LCP6204.py
@time: 2022/10/16 10:38
"""
from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums=sorted(nums)
        i,j = 0,len(nums)-1
        while(i<=j):
            if (nums[i]+nums[j]==0):
                return nums[j]
            elif (nums[i]+nums[j]<0):
                i+=1
            elif (nums[i]+nums[j]>0):
                j-=1
        return -1


if __name__=="__main__":
    nums=[-1,2,-3,3]
    x=3
    s=Solution()
    print(s.findMaxK(nums))