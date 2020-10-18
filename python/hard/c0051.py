# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0051.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/18 12:58
"""

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def solve(row: int, columns: int, diagonals1: int, diagonals2: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while availablePositions:
                    position = availablePositions & (-availablePositions)
                    availablePositions = availablePositions & (availablePositions - 1)
                    #记录当前选择点所处的位置，column和columns无关，小心看错。后者是用二进制表示已经占据位点的情况
                    column = bin(position - 1).count("1")
                    queens[row] = column
                    solve(row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)

        solutions = list()
        queens = [-1] * n
        row = ["."] * n
        solve(0, 0, 0, 0)
        return solutions


if __name__=="__main__":
    s=Solution()
    print(s.solveNQueens(4))