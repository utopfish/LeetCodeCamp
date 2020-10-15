# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0003lengthOfLongestSubstring.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/15 17:01
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue=[]
        max_len=0
        for i in s:
            if i in queue:
                for _ in range(queue.index(i)+1):
                    queue.pop(0)
            queue.append(i)
            max_len=max(max_len,len(queue))
        return max_len

if __name__=="__main__":
    k=" "
    s=Solution()
    print(s.lengthOfLongestSubstring(k))