package c0673;

import java.util.Arrays;

/**
 * @Author: Mr Liu Meng
 * @Date : 13:45 2020/10/31
 * @Description：
 */
public class Solution {
    public int findNumberOfLIS(int[] nums) {
        int [] dp=new int [nums.length];
        int [] count=new int[nums.length];
        Arrays.fill(dp,1);
        Arrays.fill(count,1);
        for (int i=0;i<nums.length;i++){
            for(int j=0;j<i;j++){
                if (nums[i]>nums[j]){
                    if (dp[j]+1>dp[i]){
                        dp[i]=dp[j]+1;
                        count[i]=count[j];
                    }else if (dp[j]+1==dp[i]){
                        count[i]+=count[j];
                    }
                    dp[i]=Math.max(dp[i],dp[j]+1);
                }
            }
        }
        int res=0;
        int max_num=0;
        for (int i=0;i<nums.length;i++){
            max_num=Math.max(max_num,dp[i]);
        }

        for (int i=0;i<nums.length;i++){
            if (dp[i]==max_num){
                res+=count[i];
            }
        }
        return res;
    }
    public static void main(String[] args){
        int [] dp=new int[]{1,3,5,4,7};
        Solution s=new Solution();
        System.out.print(s.findNumberOfLIS(dp));
    }
}
