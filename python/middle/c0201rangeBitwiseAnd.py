#@Time:2020/8/23 16:10
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:c0201rangeBitwiseAnd.py
__author__ = "liuAmon"

"""
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，
返回此范围内所有数字的按位与（包含 m, n 两端点）。
"""


def rangeBitwiseAnd(self, m: int, n: int) -> int:
    shift = 0
    # 找到公共前缀
    while m < n:
        m = m >> 1
        n = n >> 1
        shift += 1
    return m << shift