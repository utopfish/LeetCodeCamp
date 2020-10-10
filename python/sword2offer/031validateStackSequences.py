#@Time:2020/9/9 16:20
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:031validateStackSequences.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack,i=[],0
        for num in pushed:
            stack.append(num)
            while stack and popped[i]==stack[-1]:
                stack.pop()
                i+=1
        return not stack