# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5536.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/11 10:49
"""

from typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        res=0
        tree=[[] for _ in range(n)]
        for f,t in roads:
            tree[f].append(t)
            tree[t].append(f)
        for t in range(n):
            for f in range(t+1,n):
                temp=tree[f]+tree[t]
                le=len(temp)
                if f in temp and t in temp:
                    le-=1
                res=max(res,le)
        return res

if __name__=="__main__":
    s=Solution()
    print(s.maximalNetworkRank())