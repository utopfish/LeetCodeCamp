# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:game.py
#@time: 2019/10/28 14:12
'''
输入：guess = [1,2,3], answer = [1,2,3]
输出：3
'''
from typing import List
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        count=0
        for i,j in zip(guess,answer):
            if i==j:
                count+=1
        return count
class Solution2:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(guess[i] == answer[i] for i in range(len(guess)))