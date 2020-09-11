# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:beke01.py
#@time: 2020/9/7 15:16
"""
3
S B J B
J B B S
S S S s
"""
n = int(input())
hand=[]
for i in range(n):
    hand.append(input().upper().split())
for t in hand:
    s=[]
    for j in range(len(t)):
        if t[j] == 'S':
            s.append(0)
        elif t[j] == 'J':
            s.append(1)
        elif t[j] == "B":
            s.append(2)
    lenght = len(s)
    ans=[0,0]
    for k in range(2):
        if abs(s[k] - s[lenght // 2 + k]) == 1:
            if s[k] < s[lenght // 2 + k]:
                ans[k] += 1
        else:
            if s[k] > s[lenght // 2 + k]:
                ans[k] += 1

    if ans[0] > ans[1]:
        print('left')
    elif ans[0] < ans[1]:
        print('right')
    else:
        print('same')
