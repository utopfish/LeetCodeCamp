#@Time:2020/9/11 14:37
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:o51reversePairs.py
__author__ = "liuAmon"
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        result = self.reversePairs(left) + self.reversePairs(right)

        # union left and right
        left.sort()
        right.sort()
        index = 0
        for j in range(len(right)):
            while index < len(left) and left[index] <= right[j]:
                index += 1
            result += (len(left) - index)
        return result


if __name__=="__main__":
    t=[7,5,6,4]
    s=Solution()
    print(s.reversePairs(t))