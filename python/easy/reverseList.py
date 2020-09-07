#@Time:2020/9/7 14:00
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:reverseList.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def reverseList(self, head) :
        last = None
        while head:
            head.next, last ,head= last, head,head.next
        return last