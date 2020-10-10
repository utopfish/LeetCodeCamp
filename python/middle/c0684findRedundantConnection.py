#@Time:2020/9/17 14:20
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:c0684findRedundantConnection.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def find(self,e1,m):
        while m[e1]!=e1:
            m[e1]=m[m[e1]]
            e1=m[e1]
        return e1
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        m={}
        for i in range(1,len(edges)+1):
            m[i]=i
        for e in edges:
            x=self.find(e[0],m)
            y=self.find(e[1],m)
            if x==y:
                return e
            else:
                m[x]=y


if __name__=="__main__":
    input=[[1,2], [2,3], [3,4], [1,4], [1,5]]
    input=[[1,2], [1,3], [2,3]]
    s=Solution()
    print(s.findRedundantConnection(input))