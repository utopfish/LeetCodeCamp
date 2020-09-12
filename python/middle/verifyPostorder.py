#@Time:2020/9/11 19:41
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:verifyPostorder.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i,j):
            if i>=j: return True
            p=i
            while postorder[p]<postorder[j]:p+=1
            m=p
            while postorder[p]>postorder[j]:p+=1
            return p==j and  recur(i,m-1) and recur(m,j-1)
        return recur(0,len(postorder)-1)

if __name__=="__main__":
    t=[1,3,2,6,5]
    s=Solution()
    print(s.verifyPostorder(t))