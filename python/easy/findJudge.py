#@Time:2019/12/5 16:19
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:findJudge.py
from typing import List
#通过出度和入度来判断谁是法官
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        #定义入度和出度
        in_d = [0 for i in range(N)]
        out_d = [0 for i in range(N)]
        for a,b in trust:
            in_d[a-1] += 1
            out_d[b-1] += 1
        for i in range(N):
            if in_d[i] == 0 and out_d[i] == N-1:
                return i+1
        return -1