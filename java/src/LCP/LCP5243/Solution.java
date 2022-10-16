package LCP5243;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
class Solution {
        public int tupleSameProduct(int[] nums) {
            Map<Integer,Integer> hash=new HashMap<Integer,Integer>();
            int ans=0;
            for (int i=0;i<nums.length;i++){
                for (int j=i+1;j<nums.length;j++){
                    int multi=nums[i]*nums[j];
                    if(hash.containsKey(multi)){
                        ans+=hash.get(multi);
                        hash.put(multi, hash.get(multi)+1);
                    }else{
                        hash.put(multi, 1);
                    }
                }
            }
            return ans*8;
        }
    public static void main(String[] args){
        int [] arr=new int[]{2,3,5,7};
        Solution s=new Solution();
        System.out.println(s.tupleSameProduct(arr));
    }
}
