# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : 位运算.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/18 12:40
"""

# print(3&(-3))
# print(3&3)
#
#
# print(bin(5-1).count("1"))
# print(bin(12))
# print(bin(-12))
# # print(12&(-12))
# for i in range(50):
#     print(1<<i)

n=5
count=0
while n>0:
    if n&1==1:
       count+=1
    n>>=1
