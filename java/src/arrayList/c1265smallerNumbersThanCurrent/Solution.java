package c1265smallerNumbersThanCurrent;

import java.util.Arrays;
import java.util.Comparator;

/**
 * @Author: Mr Liu Meng
 * @Date : 11:02 2020/10/26
 * @Description：
 */
public class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums){
        int n=nums.length;
        int [][] data=new int[n][2];
        for (int i=0;i<n;i++){
            data[i][0]=nums[i];
            data[i][0]=i;
        }
        Arrays.sort(data, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0]-o2[0];
            }
        });
        int[] ret = new int[n];
        int prev = -1;
        for (int i = 0; i < n; i++) {
            if (prev == -1 || data[i][0] != data[i - 1][0]) {
                prev = i;
            }
            ret[data[i][1]] = prev;
        }
        return ret;
    }
}
