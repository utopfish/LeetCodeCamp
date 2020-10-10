#@Time:2019/11/11 14:42
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:c0387firstUniqChar.py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        result=[]
        for ind,i in enumerate(s):
            j=hashmap.get(i)
            if j==None:
                hashmap[i]=ind
                result.append(ind)
            else:
                try:
                    result.index(j)
                    result.pop(result.index(j))
                except:
                    pass
        return -1 if not result else result[0]
if __name__=="__main__":
    Test=Solution()
    print(Test.firstUniqChar("eee"))
