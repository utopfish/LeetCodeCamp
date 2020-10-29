package c0042;

/**
 * @Author: Mr Liu Meng
 * @Date : 21:58 2020/10/29
 * @Description：
 */
public class Solution {
    public int trap(int[] height) {
        int sum=0;
        int len=height.length;
        int [] left_hight=new int[len];
        int [] rigjt_hight=new int[len];
        for (int i =1;i<len-1;i++){
            left_hight[i]=Math.max(left_hight[i-1],height[i-1]);
        }
        for (int i=len-2;i>0;i--){
            rigjt_hight[i]=Math.max(rigjt_hight[i+1],height[i+1]);
        }
        for (int i=1;i<len-1;i++){
            int tmp=Math.min(left_hight[i],rigjt_hight[i]);
            if (tmp>height[i]){
                sum=sum+tmp-height[i];
            }
        }
        return sum;
    }
    public static void main(String[] args){
        int []height = new int[]{0,1,0,2,1,0,1,3,2,1,2,1};
        Solution s=new Solution();
        System.out.print(s.trap(height));
    }

}

