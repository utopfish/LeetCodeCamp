package c0830;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * @Author: Mr Liu Meng
 * @Date : 12:23 2021/1/5
 * @Description：
 */
class Solution {
    public List<List<Integer>> largeGroupPositions(String s) {
        int start=0;
        char [] charArr=s.toCharArray();
        List<List<Integer>> ret=new ArrayList<List<Integer>>();
        for (int i=0;i<=charArr.length;i++){
            if (i==charArr.length ||(i>0 && charArr[i]!=charArr[i-1])){
                if (i-start>2){
                    //添加数组更优雅的写法
                    ret.add(Arrays.asList(start,i-1));
                }
                start=i;
            }
        }
        return ret;
    }
    public static void main(String[] args){
        Solution s=new Solution();
        String s1 = "aaa";
        System.out.println(s.largeGroupPositions(s1));
    }
}
