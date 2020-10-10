# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:c0036isValidSuduku.py
#@time: 2019/11/10 11:56
from  typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for i in range(9)]
        col = [{} for i in range(9)]
        bor = [{} for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num != '.':

                    board_num = (i // 3) * 3 + (j // 3)
                    row[i][num] = row[i].get(num, 0) + 1
                    col[j][num] = col[j].get(num, 0) + 1
                    bor[board_num][num] = bor[board_num].get(num, 0) + 1
                    if row[i][num] > 1 or col[j][num] > 1 or bor[board_num][num] > 1:
                        return False
        return True