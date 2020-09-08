#@Time:2020/9/8 10:06
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:combine.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dsf(path,list_nums,k):#path:当前选定的组合，list_nums:待选元素的集合，k:还需选择的元素个书
            if k==0:
                return path
            res=[]
            for i in range(len(list_nums)):
                tem=dsf(path+[list_nums[i]],list_nums[list_nums.index(list_nums[i])+1:],k-1)
                res = res+[tem] if tem and isinstance(tem[0],int)  else res+tem#返回的结果可能是List[int]，或者List[List[int]]，分别进行处理
            return res
        return dsf([],list(range(1,n+1)),k)
#减少一个参数数组不必要的操作，并设置全局变量
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k: return []
        if k == 1: return [[i] for i in range(1, n+1)]
        res=[]
        def helper(path,k):
            if k==0:res.append(path);return
            for i in range(path[-1]+1,n+1):
                helper(path+[i],k-1)
            return
        for i in range(1,n):
            helper([i], k-1)
        return res

#加入剪枝操作，速度提高了近10倍
class Solution3:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k: return []
        if k == 1: return [[i] for i in range(1, n+1)]
        res=[]
        def helper(path,deep):
            if deep==k:res.append(path);
            return
            for i in range(path[-1]+1,n+deep+2-k):helper(path+[i],deep+1)
            return
        for i in range(1,n+2-k):helper([i], 1)
        return res
#继续减少一个参数，计算量可能增大
class Solution4:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k: return []
        if k == 1: return [[i] for i in range(1, n+1)]
        res=[]
        def helper(path):
            if len(path)==k:res.append(path);return
            for i in range(path[-1]+1,n+len(path)+2-k):helper(path+[i])
            return
        for i in range(1,n+2-k):helper([i])
        return res
if __name__=="__main__":
    n = 4
    k = 2
    s=Solution4()
    print(s.combine(n,k))
