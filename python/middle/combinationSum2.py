#@Time:2020/9/10 15:19
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:combinationSum2.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def dsf(path,index,t):
            for i in range(index+1,len(candidates)):
                if t-candidates[i]==0 and path+[candidates[i]] not in res:
                    res.append(path+[candidates[i]])
                elif t-candidates[i]>0:
                    dsf(path+[candidates[i]],i,t-candidates[i])
                else:
                    break
        for  i in range(len(candidates)):
            if candidates[i]==target and [candidates[i]] not in res:
                res.append([candidates[i]])
            elif target>candidates[i]:
                dsf([candidates[i]],i,target-candidates[i])
            else:
                break
        return res

if __name__=="__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    s=Solution()
    print(s.combinationSum2(candidates,target))