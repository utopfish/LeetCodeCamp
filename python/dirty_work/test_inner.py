# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : test_inner.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/27 16:01
"""
def foo(a,b):
    def inner():
        for _ in range(2):
            print(a+b)
    inner()
foo(1,2)

def inner_1(a,b):
    for _ in range(2):
        print(a + b)
def foo_1(a,b):
    inner_1(a,b)

foo_1(1,2)
# for i in range(100):
#     print("{}:".format(i),2<<i)
