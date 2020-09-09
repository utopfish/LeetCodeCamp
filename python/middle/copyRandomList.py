#@Time:2020/9/9 11:32
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:copyRandomList.py
__author__ = "liuAmon"
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited={}
        def getClone(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    new_node=Node(node.val,None,None)
                    visited[node]=new_node
                    return visited[node]
            return None
        if not head :return None
        old_node=head
        new_node=Node(head.val,None,None)
        visited[head]=new_node
        while old_node:
            new_node.next=getClone(old_node.next)
            new_node.random=getClone(old_node.random)

            new_node=new_node.next
            old_node=old_node.next
        return visited[head]