# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : 0145postorderTraversal.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/9/29 19:30
"""
"""
简单题，今天太饿了，明天试试能否用今天看到地yield 和next来解决，不知道是否空间复杂度能降低
"""
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def post(root):
            if not root:
                return
            post(root.left)
            post(root.right)

            nonlocal res
            res.append(root.val)
            return

        post(root)
        return res