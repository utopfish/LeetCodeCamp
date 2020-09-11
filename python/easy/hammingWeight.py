#@Time:2020/9/8 16:09
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:hammingWeight.py
__author__ = "liuAmon"

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

if __name__=="__main__":
    w=2
    print(w>>1)