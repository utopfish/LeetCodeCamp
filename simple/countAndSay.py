#@Time:2019/11/13 15:09
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:countAndSay.py

class Solution:
    '''
    题目比较难懂
    '''
    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1,n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1,len(prev_person)):
                if prev_person[j] == num:count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person
if __name__=="__main__":
    Test=Solution()
    print(Test.countAndSay(5))