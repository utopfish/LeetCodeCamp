package c0039;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @Author: Mr Liu Meng
 * @Date : 15:20 2020/10/27
 * @Description：
 */
class Solution {
    public void dfs(List<Integer> cur_val,int t,List<List<Integer>> res,int[] candidates){
        for (int i =Arrays.binarySearch(candidates,cur_val.get(cur_val.size()-1));i<candidates.length;i++){
            if (candidates[i]<t){
                cur_val.add(candidates[i]);
                dfs(cur_val,t-candidates[i],res,candidates);
                cur_val.remove(cur_val.size()-1);
            }else if (candidates[i]==t){
                cur_val.add(candidates[i]);
                res.add(new ArrayList<Integer>(cur_val));
                cur_val.remove(cur_val.size()-1);
            }else{
                break;
            }
        }
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res=new ArrayList<List<Integer>>();
        Arrays.sort(candidates);

        for (int i =0 ;i<candidates.length;i++){
            if (candidates[i]<target){
                List<Integer> tmp=new ArrayList<>();
                tmp.add(candidates[i]);
                dfs(tmp,target-candidates[i],res,candidates);
            }else if (candidates[i]==target){
                List<Integer> tmp=new ArrayList<>();
                tmp.add(candidates[i]);
                res.add(tmp);
            }else{
                break;
            }
        }
        return res;
    }
    public static void  main(String[] args){
        int [] candiatates=new int[]{2,3,5};
        int target=8;
        Solution s=new Solution();
        System.out.println(s.combinationSum(candiatates,target));
    }
}
