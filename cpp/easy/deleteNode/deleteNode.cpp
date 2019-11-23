//
// Created by pro on 2019/11/19.
//
#include "../../nodeBase.h"
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};
int main(){
    vector<int> nums={2, 7, 11, 15};
    ListNode *t=create(nums);
    print(t);
    Solution test;
    test.deleteNode(t);
    print(t);
}