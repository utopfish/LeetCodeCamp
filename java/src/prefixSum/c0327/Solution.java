package c0327;

/**
 * @Author: Mr Liu Meng
 * @Date : 12:47 2020/11/7
 * @Description：
 */
public class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        int count=0;
        int [] p=new int[nums.length+1];
        for (int i=1;i<nums.length+1;i++){
            int tmp_sum=0;
            for (int j=1;j<=i;j++){
                tmp_sum+=nums[j-1];
            }
            p[i]=tmp_sum;
        }
        for (int i=1;i<nums.length+1;i++){
            for (int j=0;j<i;j++){
                if ((p[i]-p[j])>=lower && (p[i]-p[j]<=upper)){
                    count++;
                }
            }

        }
        return count;
    }
    public static void main(String[] args){



        int [] nums=new int[]{-2147483647,0,-2147483647,2147483647};
        int lower=-564;
        int upper=3864;
        Solution s=new Solution();
        System.out.print(s.countRangeSum(nums,lower,upper));
    }
}
