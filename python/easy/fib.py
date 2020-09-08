#@Time:2020/9/8 16:05
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:fib.py
__author__ = "liuAmon"

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        a,b=0,1
        for i in range(1,n):
            a,b=b,(a+b)
        return b%1000000007

if __name__=="__main__":
    s=Solution()
    print(s.fib(3))