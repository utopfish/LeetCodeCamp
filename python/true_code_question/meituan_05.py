# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:meituan_05.py
#@time: 2020/9/20 11:09

a,b,c,n=map(int,input().split())
q=[]
origin=[[0,a],[b,c]]
def find(x):
    for i in range(20):
        if 2**i<x<=2**(i+1):
            return x-2**i
for _ in range(n):
    i=list(map(int,input().split()))
    [x, y] = i
    score = 0
    while x > 2 or y > 2:
        if x // y > 2:
            score += b
            x = find(x)
        elif y // x > 2:
            score += a
            y = find(y)
        else:
            score += c
            x = find(x)
            y = find(y)

    score += origin[x - 1][y - 1]
    print(score)

