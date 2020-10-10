#@Time:2020/9/18 10:51
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:c0047permuteUnique.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=set()
        def find(path,left):
            if len(left)<=1:
                res.add(tuple(path+left))
                return
            for i in range(len(left)):
                find (path+[left[i]],left[:i]+left[i+1:])
        for i in range(len(nums)):
            find([nums[i]],nums[:i]+nums[i+1:])
        res=[list(i) for i in res]
        return res
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:

                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0:
            return []

        nums.sort()

        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
        return res

if __name__=="__main__":
    input= [1,1,2]
    s=Solution()
    print(s.permuteUnique(input))