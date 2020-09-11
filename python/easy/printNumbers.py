#@Time:2020/9/7 13:27
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:printNumbers.py
__author__ = "liuAmon"
from typing import List
"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
"""
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        s=''
        for _ in range(n):
            s+='9'
        return [i for i in range(1,int(s)+1)]
#简化
class Solution2:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1,10**n)]
#继续简化
class Solution3:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1,10**n))