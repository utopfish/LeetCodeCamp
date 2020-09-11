# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:beke03.py
#@time: 2020/9/7 15:29
"""

2
2 2 1
1
1
2 2 1
1
1
"""
times = int(input())
global  res

def dfs(stack, nums):
    global res
    if len(stack) == n:
        res += 1
        return
    flag = stack[-1]
    a = nums[flag]
    for i in range(m):
        if i  not in a:
            stack.append(i)
            dfs(stack, nums)
            del stack[-1]


for i in range(times):
    res=0
    n, m, k = map(int, input().split())
    nums = []
    for j in range(m):
        nums.append(list(map(int, input().split())))
    sk = []
    for i in range(n):
        sk.append(i)
        dfs(sk, nums)
        del sk[-1]
    print(res)