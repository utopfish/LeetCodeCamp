# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0845longestMountain.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/25 14:10
"""
from typing import List
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res=0
        tmp=[]
        for i in range(1,len(A)-1):
            if A[i-1]< A[i] and A[i+1]<A[i]:
                tmp.append(i)
        for t in tmp:
            l=t-1
            r=t+1
            while l>0 and A[l-1]<A[l]:
                l-=1
            while r<len(A)-1 and A[r+1]<A[r]:
                r+=1
            res=max(res,r-l+1)
        return res

if __name__=="__main__":
    A=[2,1,4,7,3,2,5]
    s=Solution()
    print(s.longestMountain(A))