class Solution:
    def findMaxSubstr(self , str ):
        # write code here
        wind={}
        max_len=0
        max_substr=""
        start=0
        for i in range(len(str)):
            if str[i] in wind.keys()and  wind[str[i]]>=start:
                start=wind[str[i]]+1
            else:
                if i-start+1>max_len:
                    max_len=i-start+1
                    max_substr=str[start:i+1]
            wind[str[i]]=i
        return max_substr

if __name__=="__main__":
    str="abcdbcdcbabcdefggcwa"
    s=Solution()
    print(s.findMaxSubstr(str))