# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0834sumOfDistancesInTree.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/10 12:17
"""
from typing import List
#https://leetcode-cn.com/problems/sum-of-distances-in-tree/solution/shou-hua-tu-jie-shu-zhong-ju-chi-zhi-he-shu-xing-d/
"""
通过对问题进行拆分，变成求子树节点到本身的距离
"""
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(N)]
        nodeNum=[1 for _ in range(N)]
        distSum=[0 for _ in range(N)]
        for edge in edges:
            baba,erza=edge
            graph[baba].append(erza)
            graph[erza].append(baba)
        def postOrder(erza,baba):
            neighbors=graph[erza]
            for neighbor in neighbors:
                if neighbor==baba:
                    continue
                postOrder(neighbor,erza)
                nodeNum[erza]+=nodeNum[neighbor]
                distSum[erza]+=nodeNum[neighbor]+distSum[neighbor]
        def preOder(erza,baba):
            neighbors=graph[erza]
            for neighbor in neighbors:
                if neighbor==baba:
                    continue
                distSum[neighbor]=distSum[erza]-nodeNum[neighbor]+(N-nodeNum[neighbor])
                preOder(neighbor,erza)
        postOrder(0,-1)
        preOder(0,-1)
        return distSum

if __name__=="__main__":
    N = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    s=Solution()
    print(s.sumOfDistancesInTree(N,edges))