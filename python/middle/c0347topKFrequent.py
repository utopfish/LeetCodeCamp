#@Time:2020/9/7 13:15
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:c0347topKFrequent.py
__author__ = "liuAmon"
import heapq
import collections
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums: res[i] = res.get(i, 0) + 1
        res = sorted(res.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return [i[0] for i in res[:k]]
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans



if __name__=="__main__":
    s=Solution2()
    nums = [1,1,1,2,2,3]
    k = 2
    print(s.topKFrequent(nums,k))