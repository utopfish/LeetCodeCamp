#@Time:2020/9/8 13:29
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:mergeTwoLists.py
__author__ = "liuAmon"


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def createListNode(ln):
    p=ListNode(0)
    begin=p
    for i in ln:
        node=ListNode(i)
        p.next=node
        p=p.next
    return begin.next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p=begin=ListNode(0)
        while l1 and l2:
            if l1.val <l2.val:
                p.next,l1=l1,l1.next
            else:
                p.next ,l2= l2,l2.next
            p = p.next
        p.next=l1 if l1 else l2
        return begin.next

if __name__=="__main__":
    l1=createListNode([1,2,4])
    l2 = createListNode([1, 3, 4])
    s=Solution()
    t=s.mergeTwoLists(l1,l2)
    while t:
        print(t.val)
        t=t.next