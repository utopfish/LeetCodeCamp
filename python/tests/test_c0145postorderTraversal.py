# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : test_c0145postorderTraversal.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/9/30 11:12
"""
import pytest
from python.Tree import *
from python.middle.c0145postorderTraversal import Solution,Solution2
def test_1():
    num = list(range(100000))
    root = create(None, num, 0)
    s = Solution()
    s.postorderTraversal(root)
    assert  1==1
def test_2():
    num = list(range(100000))
    root = create(None, num, 0)
    s = Solution2()
    s.postorderTraversal(root)
    assert 1==1
if __name__=="__main__":
    pytest.main()