# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0116connect.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/15 15:37
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur=[root]
        while cur!=[]:
            new_cur=[]
            for i in range(len(cur)-1):
                if cur[i]:
                    cur[i].next=cur[i+1]
                    new_cur.extend([cur[i].left,cur[i].right])
            if cur[-1]:
                new_cur.extend([cur[-1].left,cur[-1].right])
            cur=new_cur
        return root