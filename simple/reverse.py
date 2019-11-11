#@Time:2019/11/11 14:27
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:reverse.py
class Solution:
    def reverse(self, x: int) -> int:
        s=list(str(x))
        if s[0]=='-':
            count=1
        else:
            count=0
        for i in range(count,count+(len(s)-count)//2):
            s[i],s[-i-1+count]=s[-i-1+count],s[i]
        if int(''.join(s))<2**31-1 and int(''.join(s))>-(2**31):
            return int(''.join(s))
        else:
            return 0
if __name__=="__main__":
    Test=Solution()
    print(Test.reverse(321))
    e
