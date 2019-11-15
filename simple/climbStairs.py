#@Time:2019/11/15 15:43
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:climbStairs.py

class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1, 2]
        for i in range(2, n):
            f.append(f[i-1] + f[i-2])
        return f[n-1]
if __name__=="__main__":
    Test=Solution()
    print(Test.climbStairs(10))