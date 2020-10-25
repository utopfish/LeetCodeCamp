# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5547.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/25 10:48
"""
from typing import List
class Solution:
    def check(self,tmp):
        for j in range(1,len(tmp)-1):
            if tmp[j]-tmp[j-1]!=tmp[j+1]-tmp[j]:
                return False
        return True
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        for i in range(len(l)):
            tmp=sorted(nums[l[i]:r[i]+1])
            res.append(self.check(tmp))
        return res

if __name__=="__main__":
    nums = [4, 6, 5, 9, 3, 7]
    l = [0, 0, 2]
    r = [2, 3, 5]
    s=Solution()
    print(s.checkArithmeticSubarrays(nums,l,r))