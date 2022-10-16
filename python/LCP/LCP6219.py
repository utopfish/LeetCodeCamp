"""
@author: liuAmon
@contact:utopfish@163.com
@file: LCP6219.py
@time: 2022/10/16 10:46
"""
from typing import List



class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l, r1, r2, ret = -1, -1, -1, 0
        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK: l = i
            if nums[i] == maxK: r1 = i
            if nums[i] == minK: r2 = i
            ret += max(0, min(r1, r2) - l)
        return ret

# 作者：newhar
# 链接：https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/solution/fen-xi-ding-jie-zi-shu-zu-de-xing-zhi-yi-qusi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    nums = [1, 1, 1, 1]
    x = 1
    y = 1
    s = Solution()
    print(s.countSubarrays(nums, x, y))
