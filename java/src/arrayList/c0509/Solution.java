package c0509;

import c0042.Soultion2;

/**
 * @Author: Mr Liu Meng
 * @Date : 12:59 2021/1/4
 * @Description：
 */
public class Solution {
    public int fib(int n) {
        if (n<2){
            return n;
        }
        int a=1;
        int b=1;
        int tmp=0;
        for (int i=2;i<n;i++){
            tmp=a+b;
            a=b;
            b=tmp;
        }
        return b;
    }
    public static void main(String[] args){
        Solution s=new Solution();
         System.out.println(s.fib(4));
    }
}
