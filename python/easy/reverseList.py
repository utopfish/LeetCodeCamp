#@Time:2020/9/7 14:00
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:reverseList.py
__author__ = "liuAmon"
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#暴力法，用栈存数据
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        mark=head
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        head=mark
        while head:
            head.val=l.pop()
            head=head.next
        return mark

#大佬的方法，理解起来相对麻烦，最后的耗时与上面方法相近
class Solution2:
    def reverseList(self, head) :
        last = None
        while head:
            head.next, last ,head= last, head,head.next
        return last