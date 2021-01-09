package c0124;

/**
 * @Author: Mr Liu Meng
 * @Date : 22:44 2021/1/9
 * @Description：
 */
public class Solution {
    public int maxPathSum(TreeNode root) {
        int[] ret=helper(root);
        return  ret[1];

    }
    public int[] helper(TreeNode root){
        if (root==null){
            return new int[2];
        }
        if (root.left==null && root.right==null){
            return new int[]{root.val,root.val};
        }
        int[] ret=new int[2];
        ret[1]=Integer.MIN_VALUE;
        ret[0]=Integer.MIN_VALUE;
        int []left=helper(root.left);
        int [] right=helper(root.right);
        int maxLeft=Math.max(0, root.val)+Math.max(0,left[0]);
        int maxRight=Math.max(0, root.val)+Math.max(0,right[0]);
        ret[0]=Math.max(maxLeft, maxRight);
        ret[1]=Math.max(left[1],right[1]);
        ret[1]=Math.max(ret[1], left[0]+root.val+right[0]);
        return ret;
    }
    public static void main(String[] args){
        Integer[]li=new Integer[]{2,-1};
        TreeNode root=TreeNode.arrayToTreeNode(li);
        Solution s=new Solution();
        System.out.println(s.maxPathSum(root));
    }
}
