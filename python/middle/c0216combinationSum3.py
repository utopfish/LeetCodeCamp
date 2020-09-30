#@Time:2020/9/11 13:49
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:c0216combinationSum3.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def dsf(path,target,lenght):
            for  i in range(path[-1]+1,10):
                if target==i and lenght==k-1:
                    res.append(path+[i])
                    break
                elif target>i:
                    dsf(path+[i],target-i,lenght+1)
                elif target<i:
                    break
        for i in range(1,10):
            if n==i and k==1:
                res.append([i])
            elif n>i:
                dsf([i],n-i,1)
            else:
                break
        return res

if __name__=="__main__":
    k = 3
    n = 9
    s=Solution()
    print(s.combinationSum3(k,n))