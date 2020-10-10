# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:o48lengthOfLongestSubstring.py
#@time: 2019/10/28 14:55
class Solution:
    def get_key(self,dict, value):
        temp=[k for k, v in dict.items() if v == value]
        return temp[0]
    def lengthOfLongestSubstring(self, s: str) -> int:
        max=0
        hashmap={}
        count=0
        for i in s:
            j=hashmap.get(i)
            if j!=None:
                for k in range(len(hashmap)):
                    if k <=j:
                        del hashmap[self.get_key(hashmap,k)]
                    else:
                        hashmap[self.get_key(hashmap, k)]-=j+1
                count-=j+1
            hashmap[i]=count
            count+=1
            if count > max:
                max = count
        return max

class Solution2:
    '''
    使用滑动窗口
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            lookup.add(s[i])
        return max_len
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp=0
        maxlen = 0
        res = {}
        for i in range(len(s)):
            j=res.get(s[i],-1)
            res[s[i]]=i
            dp=dp+1 if dp<j-1 else j-1
            maxlen =max(maxlen,dp)

        return maxlen
if __name__=="__main__":
    s="dvdf"
    test=Solution3()
    print(test.lengthOfLongestSubstring(s))