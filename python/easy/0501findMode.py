#@Time:2020/9/24 12:31
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:0501findMode.py
__author__ = "liuAmon"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        res={}
        def find(root):
            if root:
                res[root.val]=res.get(root.val,0)+1
                find(root.left)
                find(root.right)
        find(root)
        res=sorted(res.items(),key=lambda x:x[1],reverse=True)
        r=[]
        for i in res:
            if i[1]==res[0][1]:
                r.append(i[0])
        return r





