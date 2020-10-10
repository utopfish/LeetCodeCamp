# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : o16myPow.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/10 17:12
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quick_pow(x,y):
            tmp=x
            res=1
            while y>0:
                if y&1==1:
                    res*=tmp
                y>>=1
                tmp*=tmp
            return res
        if n>0:return quick_pow(x,n)
        else:
            return 1/quick_pow(x,-n)

if __name__=="__main__":
    s=Solution()
    print(s.myPow(2,10))