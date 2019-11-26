//
// Created by pro on 2019/11/26.
//
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return ismirror(root,root);
    }
    bool ismirror(TreeNode* t1,TreeNode* t2)
    {
        if(t1==NULL&&t2==NULL)//都为空
            return true;
        if(t1==NULL||t2==NULL)//有一个为空
            return false;
        return (t1->val==t2->val)&&ismirror(t1->left,t2->right)&&ismirror(t1->right,t2->left);
    }
};
