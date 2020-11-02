package c0349;

import java.util.*;

/**
 * @Author: Mr Liu Meng
 * @Date : 15:30 2020/11/2
 * @Description：
 */
public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Map<Integer,Integer> hash=new HashMap<Integer,Integer>();
        Set<Integer> res=new HashSet<Integer>();
        for (int i=0;i<nums1.length;i++){
            hash.put(nums1[i],hash.getOrDefault(nums1[i],0)+1);
        }
        for (int i = 0;i<nums2.length;i++){
            if (hash.containsKey(nums2[i])){
                res.add(nums2[i]);
            }
        }
        return res.stream().mapToInt(Integer::valueOf).toArray();
    }
    public static  void  main(String[] args){
        int [] nums1=new int[]{1,2,2,1};
        int [] nums2=new int[]{2,2};
        Solution s=new Solution();
        System.out.print(s.intersection(nums1,nums2));
    }
}
