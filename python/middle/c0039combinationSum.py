#@Time:2020/9/9 10:33
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:c0039combinationSum.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dsf(cur_val,t):
            for i in range(candidates.index(cur_val[-1]),len(candidates)):
                if candidates[i]<t:
                    dsf(cur_val+[candidates[i]],t-candidates[i])
                elif candidates[i]==t:
                    res.append(cur_val+[candidates[i]])
            return
        for i in range(len(candidates)):
            if candidates[i]<target:
                dsf([candidates[i]],target-candidates[i])
            elif candidates[i]==target:
                res.append([candidates[i]])
        return res

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dsf(cur_val,t):
            for i in range(candidates.index(cur_val[-1]),len(candidates)):
                if candidates[i]<t:
                    dsf(cur_val+[candidates[i]],t-candidates[i])
                elif candidates[i]==t:
                    res.append(cur_val+[candidates[i]])
                else:
                    break
            return
        for i in range(len(candidates)):
            if candidates[i]<target:
                dsf([candidates[i]],target-candidates[i])
            elif candidates[i]==target:
                res.append([candidates[i]])
            else:
                break
        return res
if __name__=="__main__":
    candidates = [2, 3, 5]
    target = 8
    s=Solution()
    print(s.combinationSum(candidates,target))