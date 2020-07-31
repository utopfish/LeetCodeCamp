//
// Created by pro on 2020/7/31.
//
// 基础做法
class Solution1 {
public:
    string reverseLeftWords(string s, int n) {
        string res="";
        for(int i =n ; i<s.size() ; i++){
            res+=s[i];
        }
        for (int i=0 ; i<n; i++){
            res+=s[i];
        }
        return res;
    }
};
//使用切片进行，对substr，两个参数分别为起点和长度
class Solution2 {
public:
    string reverseLeftWords(string s, int n) {
        return (s+s).substr(n,s.size());
    }
};