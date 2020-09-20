#@Time:2020/9/19 14:20
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:meituan03.py
__author__ = "liuAmon"
"""
输入：
6
2 1 5 6 2 3
输出：
10
输入：
7
6 2 5 4 5 1 6
输出：
12
"""
n = int(input())
h = [int(x) for x in input().split()]

def largestarea(a):
    l = len(a)
    idx = a.index(min(a))

    value1 = a[idx] * l

    if idx != 0:
        value2 = largestarea(a[0:idx])
    else:
        value2 = 0
    if idx != l - 1:
        value3 = largestarea(a[idx + 1:l])
    else:
        value3 = 0
    return max(value1, value2, value3)


print(largestarea(h))