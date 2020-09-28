#@Time:2020/9/28 19:26
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:LCP03robot.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        dd=[[0,1],[1,0]]
        status_x=0
        status_y=0
        hash={}
        for i in obstacles:
            hash[" ".join(list(map(str,i)))]=1
        while True:
            for i in command:
                if i=="U":
                    status_x+=dd[0][0]
                    status_y+=dd[0][1]
                else:
                    status_x+=dd[1][0]
                    status_y+=dd[1][1]
                if " ".join(list(map(str,[status_x,status_y]))) in hash.keys():
                    return False
                if status_x==x and status_y==y:
                    return True


class Solution2:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:

        xi = 0
        yi = 0

        # 计算第一次执行完command后, 走过的所有坐标
        first_coor = [[0, 0]]
        for c in command:
            if c == 'R':
                xi += 1
            else:
                yi += 1
            first_coor.append([xi, yi])

        # 此时(xi, yi)也代表着初次command执行结束时走到的最后一个坐标
        # 走到目标点所需要的循环次数
        circle = min(x // xi, y // yi)

        if [x - xi * circle, y - yi * circle] not in first_coor:
            return False

        # 对每个阻碍点逐个判断，是否会走到它
        for obstacle in obstacles:
            ob_x, ob_y = obstacle[0], obstacle[1]
            # 走到阻碍点所需要的循环数（若是能走到的话）
            circle = min(ob_x // xi, ob_y // yi)
            # 判断是否会走到这个阻碍点，注意在终点之后的阻碍点可以忽略
            if ob_x <= x and ob_y <= y and [ob_x - xi * circle, ob_y - yi * circle] in first_coor:
                return False

        return True


if __name__=="__main__":
    command = "RRRUUU"
    obstacles = [[3,0]]
    x = 3
    y = 3
    s=Solution2()
    print(s.robot(command,obstacles,x,y))