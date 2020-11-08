# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5563.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/11/8 11:00
"""
import heapq
from typing import List
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        h=[]
        count=0
        for i in inventory:
            heapq.heappush(h,-i)
        while orders>0:
            top1=-heapq.heappop(h)
            if len(h)>0:
                top2=-heapq.nsmallest(1, h)[0]
            else:
                top2=0
            range_length=min(top1-top2+1,orders)
            count+=((top1-range_length+1+top1)*range_length/2)
            count = count % (10**9+7)
            orders-=range_length
            heapq.heappush(h,-(top2-1))
        return int(count)


class Solution2:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        mod = 10 ** 9 + 7

        # 二分查找 T 值
        l, r, T = 0, max(inventory), -1
        while l <= r:
            mid = (l + r) // 2
            total = sum(ai - mid for ai in inventory if ai >= mid)
            if total <= orders:
                T = mid
                r = mid - 1
            else:
                l = mid + 1

        range_sum = lambda x, y: (x + y) * (y - x + 1) // 2

        rest = orders - sum(ai - T for ai in inventory if ai >= T)
        ans = 0
        for ai in inventory:
            if ai >= T:
                if rest > 0:
                    ans += range_sum(T, ai)
                    rest -= 1
                else:
                    ans += range_sum(T + 1, ai)

        return ans % mod
if __name__=="__main__":
    inventory = [773160767]
    orders = 252264991
    #预期结果 70267492
    # inventory =[3,5]
    # orders =  6
    s=Solution2()
    print(s.maxProfit(inventory,orders))