# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0229majorityElement.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/10 16:34
"""
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash = {}
        for i in nums:
            hash[i]=hash.get(i,0)+1
        s=sorted(hash.items(), key=lambda d: d[1],reverse=True)
        temp=[]
        for i in s:
            if i[1]>len(nums)//3:
                temp.append(i[0])
        return temp