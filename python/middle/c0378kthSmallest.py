# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:c0378kthSmallest.py
#@time: 2019/10/28 14:31
class Solution():
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        # 计算小于等于目标值的元素个数，根据递增规则，从右上角开始查找
        def count_num(m, target):
            i = 0
            j = len(m) - 1
            ans = 0
            while i < len(m) and j >= 0:
                if m[i][j] <= target:
                    ans += j + 1
                    i += 1
                else:
                    j -= 1
            return ans

        #  思路：左上角元素最小，右下角元素最大，计算小于等于中间值的元素个数
        left = matrix[0][0]
        right = matrix[-1][-1]
        # 二分法查找
        while left < right:
            mid = (left + right) >> 1
            # print(' mid = ', mid)
            count = count_num(matrix, mid)
            # print('count = ', count)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left


if __name__=="__main__":
    atrix = [
                [1, 5, 9],
                [10, 11, 13],
                [12, 13, 15]
            ]
    k = 8
    T=Solution()
    print(T.kthSmallest(atrix,k))
