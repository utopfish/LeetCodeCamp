package c0300;

/**
 * @Author: Mr Liu Meng
 * @Date : 12:39 2020/11/14
 * @Description：
 */
class Solution {
    public int lengthOfLIS(int[] nums) {
        int max_len=0;
        if (nums.length<2){
            return nums.length;
        }
        int start=0;
        for (int end =1;end<nums.length;end++){

            if (nums[end] <= nums[end-1]){
                max_len=Math.max(max_len,end-start);
                start=end;
            }

        }
        return max_len;
    }
    public static void main(String[] args){
        int [] arr=new int[]{10,9,2,5,3,7,101,18};
        Solution s=new Solution();
        System.out.print(s.lengthOfLIS(arr));
    }
}