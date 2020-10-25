# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5548.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/25 10:51
"""
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row=len(heights)
        col=len(heights[0])
        distance=[[float('inf')]* col for _ in range(row)]
        distance[0][0]=0
        def bsf(queue):
            dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            while queue:
                x, y,old_x,old_y = queue.pop(0)

                for i in dd:
                    new_x = x + i[0]
                    new_y = y + i[1]
                    if 0 <= new_x < row and 0 <= new_y < col and (new_x,new_y)!=(old_x,old_y ):
                        if distance[new_x][new_y]>max(distance[x][y],abs(heights[new_x][new_y] - heights[x][y])):
                            distance[new_x][new_y]=max(distance[x][y],abs(heights[new_x][new_y] - heights[x][y]))
                            queue.append((new_x,new_y,x,y))
        bsf([(0,0,-1,-1)])
        return  distance[-1][-1]

class Solution:
    min_cost = float('inf')
    def find(self,x,y,visited,row,col,heights,path_cost):
        dd = [[0, 1],[1, 0], [0, -1],  [-1, 0]]
        mark=[float('inf') for _ in range(4)]
        for ind,i in enumerate(dd):
            new_x = x + i[0]
            new_y = y + i[1]
            if 0 <= new_x < row and 0 <= new_y < col and visited[new_x][new_y] == -1 and abs(
                    heights[new_x][new_y] - heights[x][y]) <= self.min_cost:
                if new_x==row-1 and new_y==col-1:
                    self.min_cost = min(self.min_cost, max(path_cost,abs(
                        heights[new_x][new_y] - heights[x][y])))
                else:
                    mark[ind]=max(path_cost,abs(
                        heights[new_x][new_y] - heights[x][y]))
        if min(mark)==float('inf'):
            return
        ind=mark.index(min(mark))
        new_x=x+dd[ind][0]
        new_y=y+dd[ind][1]
        visited[new_x][new_y] = 1
        path_cost=max(path_cost,abs(
            heights[new_x][new_y] - heights[x][y]))
        self.find(new_x, new_y, visited, row, col, heights, path_cost)
        visited[new_x][new_y] = -1

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row=len(heights)
        col=len(heights[0])
        visited = [[-1] * col for _ in range(row)]
        self.find(0,0,visited,row,col,heights,0)
        return self.min_cost if self.min_cost!=float('inf') else 0
if __name__=="__main__":
    heights = [[1,2,3],[3,8,4],[5,3,5]]
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    #heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    heights =[[8,3,2,5,2,10,7,1,8,9],[1,4,9,1,10,2,4,10,3,5],[4,10,10,3,6,1,3,9,8,8],[4,4,6,10,10,10,2,10,8,8],[9,10,2,4,1,2,2,6,5,7],[2,9,2,6,1,4,7,6,10,9],[8,8,2,10,8,2,3,9,5,3],[2,10,9,3,5,1,7,4,5,6],[2,3,9,2,5,10,2,7,1,8],[9,10,4,10,7,4,9,3,1,6]]
    #heights=[[3]]
    s=Solution()
    print(s.minimumEffortPath(heights))


