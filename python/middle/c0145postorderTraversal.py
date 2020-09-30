# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0145postorderTraversal.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/9/29 19:30
"""
"""
简单题，今天太饿了，明天试试能否用今天看到地yield 和next来解决，不知道是否空间复杂度能降低.
+ yield 似乎不能在这里使用，在遍历树中存在迭代的问题，无法简单用yield处理。
"""
from typing import List
import pytest
from python.Tree import *
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def post(root):
            if not root:
                return
            post(root.left)
            post(root.right)

            res.append(root.val)
            return
        post(root)
        return res

class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def post(root):
            if not root:
                return

            if root.left:
                for x in post(root.left):
                    yield x

            if root.right:
                for x in post(root.right):
                    yield x

            yield root
        res=[i.val for i in post(root)]
        return res

def test_1():
    num = list(range(10000))
    root = create(None, num, 0)
    s = Solution()
    s.postorderTraversal(root)

def test_2():
    num = list(range(10000))
    root = create(None, num, 0)
    s = Solution2()
    s.postorderTraversal(root)
if __name__=="__main__":
    pytest.main("-s c0145postorderTraversal.py")