#@Time:2020/9/14 13:05
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:exist.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dd=[[-1,0],[1,0],[0,1],[0,-1]]
        visited=set()
        def find(x,y,index):
            if board[x][y]==word[index]:
                if index==len(word)-1:return True
                else:
                    res=False
                    visited.add((x,y))
                    for d in dd:
                        new_x=x+d[0]
                        new_y=y+d[1]
                        if 0<=new_x<len(board) and 0<=new_y<len(board[0]) and (new_x,new_y) not in visited:
                            if find(new_x,new_y,index+1):
                                res=True
                                break
                    visited.remove((x,y))
                    return res
            else:return False
        for i in range(len(board)):
            for j in range(len(board[1])):
                    if find(i,j,0):
                        return True
        return False

if __name__=="__main__":
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    s=Solution()
    print(s.exist(board,word))