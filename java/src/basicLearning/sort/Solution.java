package basicLearning.sort;

public class Solution {
    public void exch(int[] nums,int i,int j){
        int t=nums[i];
        nums[i]=nums[j];
        nums[j]=t;
    }
    public void sorts(int [] nums,int i,int j){
        if (i>=j)return;
        int mid=quickSort(nums,i,j);
        sorts(nums,i,mid-1);
        sorts(nums,mid+1,j);
    }
    public int  quickSort(int [] nums,int low,int hight){
        int i=low;int j=hight+1;
        int val=nums[low];
        while (true){
            while (nums[++i]<val) if (i==hight)break;
            while (nums[--j]>val) if (j==low)break;
            if (i>=j)break;
            exch(nums,i,j);
        }
        exch(nums,low,j);
        return j;
}
}
