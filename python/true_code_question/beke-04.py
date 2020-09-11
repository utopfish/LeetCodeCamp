# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:beke-04.py
#@time: 2020/9/7 16:02
n=int(input())
nums=[]
for i in range(2):
    nums.append(list(map(int,input().split())))
min_life=int(1e9)
life=0
for i in range(n-1,-1,-1):
    life-=nums[0][i]
    min_life=min(life,min_life)
    life+=nums[1][i]
for i in range(n,2*n):
    life-=nums[0][i]
    min_life=min(life,min_life)
    life+=nums[1][i]
min_life2=int(1e9)
life=0
for i in range(n,2*n):
    life-=nums[0][i]
    min_life2=min(life,min_life2)
    life+=nums[1][i]
for i in range(n-1,-1,-1):
    life-=nums[0][i]
    min_life2=min(life,min_life2)
    life+=nums[1][i]

print(min(1-min_life,1-min_life2))