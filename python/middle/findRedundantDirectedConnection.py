#@Time:2020/9/17 15:08
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:findRedundantDirectedConnection.py
__author__ = "liuAmon"
from typing import List
class unionFind():
    def __init__(self,n):
        self.ancetor=list(range(n))
        self.sz=[1 for _ in range(n)]
    def find(self,node):
        while self.ancetor[node]!=node:
            self.ancetor[node]=self.ancetor[self.ancetor[node]]
            node=self.ancetor[node]
        return node
    def union(self,node1,node2):
        p1=self.find(node1)
        p2=self.find(node2)
        if self.sz[p1]<self.sz[p2]:
            self.ancetor[p1]=p2
            self.sz[p2]+=self.sz[p1]
        else:
            self.ancetor[p2]=p1
            self.sz[p1]+=self.sz[p2]

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        size=len(edges)
        uf=unionFind(size+1)
        parent=list(range(size+1))
        conflict=-1
        cyc=-1
        for index,e in enumerate(edges):
            if parent[e[1]]!=e[1]:
                conflict=index
            else:
                parent[e[1]]=e[0]
                if uf.find(e[0])==uf.find(e[1]):
                    cyc=index
                else:
                    uf.union(e[0],e[1])
        if conflict<0:
            return edges[cyc]
        else:
            conflictEdges=edges[conflict]
            if cyc>=0:
                return [parent[conflictEdges[1]],conflictEdges[1]]
            else:
                return conflictEdges

