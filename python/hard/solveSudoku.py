# @Time:2020/9/15 9:42
# @Author:liuAmon
# @e-mail:utopfish@163.com
# @File:solveSudoku.py
__author__ = "liuAmon"
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        valid = False
        def dfs(pos):
            nonlocal valid
            if pos == len(space):
                valid=True
                return True
            x, y = space[pos]
            for i in range(9):
                if not cow[x][i] and not col[y][i] and not black[x // 3][y // 3][i]:
                    cow[x][i] = col[y][i] = black[x // 3][y // 3][i] = True
                    board[x][y] = str(i + 1)
                    dfs(pos + 1)
                    cow[x][i] = col[y][i] = black[x // 3][y // 3][i] = False
                if valid:
                    return

        cow = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        black = [[[False] * 9 for _a in range(9)] for _b in range(9)]
        space = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    space.append((i, j))
                else:
                    dig = int(board[i][j]) - 1
                    cow[i][dig] = col[j][dig] = black[i // 3][j // 3][dig] = True
        dfs(0)


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    s = Solution()
    print(s.solveSudoku(board))
