#@Time:2020/9/28 19:08
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:LCP02fraction.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        a = b = -1
        num_length = len(cont)-1
        for i in range(num_length,-1,-1):
            if i == num_length:
                a,b = cont[-1],1
            else:
                a,b = cont[i]*a+b,a

        return [a,b]

if __name__=="__main__":
    cont = [3, 2, 0, 2]
    s=Solution()
    print(s.fraction(cont))