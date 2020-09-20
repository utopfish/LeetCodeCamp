#@Time:2020/9/20 17:02
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:findRepeatNumber.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hash={}
        for i in nums:
            if i in hash.keys():
                return i
            hash[i]=hash.get(i,0)+1