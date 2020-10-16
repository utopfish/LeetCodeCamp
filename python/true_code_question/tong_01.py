# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:tong_01.py
#@time: 2020/9/27 15:12

class Node:
    val=None
    left=None
    right=None

    def put(self,val):
        self.val=val

def addRight(root,left,val):
    temp=Node()
    temp.put(val)
    if left=="left":
        root.left=temp
    else:
        root.right=temp
    return  root
