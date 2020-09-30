# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : Tree.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/9/30 10:07
@Desc    : 关于二叉树的基础操作
"""


class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right



def create(root,numbers,i):
    if i<len(numbers):
        if not numbers[i]:
            return None
        else:
            root=TreeNode(numbers[i])
            root.left=create(root.left,numbers,i+1)
            root.right=create(root.right,numbers,i+2)
            return root
    return root

if __name__=="__main__":
    num=[1,None,2,3]
    root=create(None,num,0)
    print(root)

