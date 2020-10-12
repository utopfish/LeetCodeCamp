# -*- coding: utf-8 -*-
"""
@Project :  PyCharm
@File    : c0530getMinimumDifference.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/12 
"""


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = float('inf')
        # pre 记录前驱节点
        pre = -1

        def dfs(root):
            nonlocal ans, pre
            if not root:
                return

            dfs(root.left)
            # 节点值处理，
            if pre != -1:
                # 比较相邻元素差值，取最小值
                ans = min(ans, root.val - pre)
            # 维护更新 pre
            pre = root.val
            dfs(root.right)

        dfs(root)

        return ans