#@Time:2020/9/20 14:40
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:0078subsets.py
__author__ = "liuAmon"
from  typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        nums.sort()
        def find(path,deep):
            if deep==len(nums)-1:
                res.append(path)
            for i in range(nums.index(path[-1])+1,len(nums)):
                find(path+[nums[i]],deep+1)
            return
        for i in range(len(nums)):
            temp=[]
            for j in range(len(nums)):
                find([nums[j]],i)
        return res