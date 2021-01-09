package c0124;

/**
 * @Author: Mr Liu Meng
 * @Date : 22:44 2021/1/9
 * @Description：
 */
public class Solution {
        int maxNum=Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        helper(root);
        return maxNum;

    }
    public int helper(TreeNode root){
        if (root==null){
            return 0;
        }
        int left=Math.max(0,helper(root.left));
        int right=Math.max(0,helper(root.right));
        maxNum=Math.max(maxNum, left+right+root.val);
        return Math.max(left,right)+root.val;
    }
}
