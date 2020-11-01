# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0140.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/11/1 9:28
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        #转为set 加速查询
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for right in range(1, n + 1):
            for left in range(right - 1, -1, -1):
                if (dp[left] and (s[left:right] in wordDict)):
                    dp[right] = True
                    break

        def dfs(begin, path):
            if begin == n:
                res.append(" ".join(path))
                return
            for i in range(begin+1, n+1):
                if dp[i] and s[begin:i] in wordDict:
                    path.append(s[begin:i])
                    dfs(i, path)
                    # 之前这里使用path.remove(string[begin:i])报错，是因为存在相同的元素，导致删除错误
                    path.pop(-1)

        if dp[-1]:
            dfs(0, [])
        return res

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        #转为set 加速查询
        wordDict = set(wordDict)
        n = len(s)
        trues = [0]
        # 对能进行划分的其实位置进行单独存储，减小了时间和空间复杂度。与法二思想类似。
        for j in range(0, len(s) + 1):
            for i in trues:
                if s[i:j] in wordDict:
                    trues.append(j)
                    break

        def dfs(begin, path):
            if begin == n:
                res.append(" ".join(path))
                return
            for i in trues:
                if  s[begin:i] in wordDict:
                    path.append(s[begin:i])
                    dfs(i, path)
                    # 之前这里使用path.remove(string[begin:i])报错，是因为存在相同的元素，导致删除错误
                    path.pop(-1)
        if trues[-1]==n:
            dfs(0, [])
        return res
if __name__== "__main__":
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

    t=Solution2()
    print(t.wordBreak(s,wordDict))

