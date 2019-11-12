#@Time:2019/11/12 19:05
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:isAnagram.py

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap={}
        for i in range(len(s)):
            if hashmap.get(s[i])!=None:
                hashmap[s[i]]=hashmap.get(s[i])+1
            else:
                hashmap[s[i]]=1
        for i in t:
            if hashmap.get(i)!=None:
                hashmap[i] = hashmap.get(i) - 1
        for i in hashmap:
            if hashmap[i]!=0:
                return False
        return True
if __name__=="__main__":
    Test=Solution()
    print(Test.isAnagram("a","b"))