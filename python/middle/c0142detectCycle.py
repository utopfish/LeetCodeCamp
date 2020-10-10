# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0142detectCycle.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/10 9:57
"""


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return

        fast = slow = par = head
        fast = fast.next
        if not fast:
            return
        fast = fast.next
        slow = slow.next
        while fast and fast != slow:
            fast = fast.next
            if not fast:
                return
            fast = fast.next
            slow = slow.next
        if not fast:
            return
        while par != slow:
            par = par.next
            slow = slow.next
        return par

#思路相同，代码精简后，从19行变为9行
class Solution2(object):
    def detectCycle(self, head):
        fast=slow=head
        while True:
            if not (fast and fast.next):return
            fast,slow=fast.next.next,slow.next
            if fast==slow:break
        fast=head
        while fast!=slow:
            fast,slow=fast.next,slow.next
        return fast