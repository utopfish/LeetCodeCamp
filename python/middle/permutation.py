#@Time:2020/9/10 15:44
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:permutation.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s: return
        s=list(sorted(s))
        res=[]
        def helper(s,tmp):
            if not s: res.append(''.join(tmp))
            for i,char in enumerate(s):
                if i>0 and s[i]==s[i-1]:
                    continue
                helper(s[:i]+s[i+1:],tmp+[char])
        helper(s,[])
        return res


if __name__=="__main__":
    s = "abc"
    t=Solution()
    print(t.permutation(s))