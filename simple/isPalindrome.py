#@Time:2019/11/13 14:40
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:isPalindrome.py

class Solution:
    '''
    战胜60%
    '''
    def isPalindrome(self, s: str) -> bool:
        t=[i.lower() for i in s if i.isalnum()]
        return t==t[::-1]
class Solution:
    '''
    战胜70%
    '''
    def isPalindrome(self, s: str) -> bool:
        t=[i.lower() for i in s if i.isalnum()]
        for i,j in zip(t,t[::-1]):
            if i!=j:
                return False
        return True
if __name__=="__main__":
    Test=Solution()
    print(Test.isPalindrome("A man, a plan, a canal: Panama"))