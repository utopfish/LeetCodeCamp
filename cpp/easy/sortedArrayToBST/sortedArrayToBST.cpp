//
// Created by pro on 2019/11/28.
//
#include "../../nodeBase.h"
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.empty()) return nullptr;
        return helper(nums,0,nums.size());
    }
    TreeNode* helper(vector<int>& nums,int left, int right){
        if (left>right){
            return nullptr;
        }
        int mid=(left+right)/2;
        TreeNode *root=new TreeNode(nums[mid]);
        root->left=helper(nums,left,mid-1);
        root->right=helper(nums,mid+1,right);
        return root;
    }
};
int main(){
    vector<int> nums={2, 7, 11, 15};
    int target=9;
    Solution test;
    TreeNode* re=test.sortedArrayToBST(nums);


}