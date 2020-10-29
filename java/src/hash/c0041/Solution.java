package c0041;

/**
 * @Author: Mr Liu Meng
 * @Date : 21:16 2020/10/29
 * @Description：
 */
public class Solution {
    public int firstMissingPositive(int[] nums) {
        int len=nums.length;
        for (int i=0;i<len;i++){
            while (nums[i]>0 && nums[i]<len && nums[nums[i]-1]!=nums[i]) {
                swap(nums, i, nums[i] - 1);
            }
        }
        for (int i=0;i<len;i++){
            if (i!=nums[i]-1){
                return i;
            }
        }
        return len+1;
    }
    public void swap(int[] nums,int index1,int index2){
        int tmp=nums[index1];
        nums[index1]=nums[index2];
        nums[index2]=tmp;
    }
}
