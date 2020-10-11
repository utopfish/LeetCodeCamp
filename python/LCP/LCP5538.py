# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5538.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/11 11:25
"""
from typing import List
#自己的方法，先找数，再确定距离。思路找不到全部的集合
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        tree=[[] for _ in range(n+1)]
        res=[[] for _ in range(n)]
        for erza,baba in edges:
            tree[erza].append(baba)
            tree[baba].append(erza)

        def DFSfind(i,deep,path,baba,father):
            for neighbor in tree[baba]:
                if neighbor!=father:
                    temp = path + [neighbor]
                    temp.sort()
                    if i==deep:
                        if temp not in res[i]:
                            res[i].append(temp)
                    elif i>deep:
                        DFSfind(i,deep+1,temp,neighbor,baba)


        for i in range(1,n):
            for j in range(1,n):
                DFSfind(i,1,[j],j,-1)
        return [len(i) for i in res[1:] ]

class Solution2:
    def countSubgraphsForEachDiameter(self, n, edges):
        G = [[] for i in range(n)]
        for i, j in edges:
            G[i - 1].append(j - 1)
            G[j - 1].append(i - 1)

        def maxd(mask0):
            res = 0
            for i in range(n):
                if (1 << i) & mask0:
                    mask = mask0
                    bfs, bfs2 = [i], []
                    cur = 0
                    while bfs:
                        for i in bfs:
                            mask ^= 1 << i
                            for j in G[i]:
                                if mask & (1 << j):
                                    bfs2.append(j)
                        cur += 1
                        bfs, bfs2 = bfs2, []
                    if mask: return 0
                    res = max(res, cur - 1)
            return res

        res = [0] * (n - 1)
        for mask in range(1 << n):
            if mask & (mask - 1) == 0: continue
            d = maxd(mask)
            if d:
                res[d - 1] += 1

        return res
if __name__=="__main__":
    s=Solution2()
    n = 4
    edges = [[1, 2], [2, 3], [2, 4]]
    print(s.countSubgraphsForEachDiameter(n,edges))


