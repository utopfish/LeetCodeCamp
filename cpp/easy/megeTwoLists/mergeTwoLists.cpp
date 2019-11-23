//
// Created by pro on 2019/11/23.
//
#include "../../nodeBase.h"
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL) return l2;
        else if (l2 == NULL) return l1;
        else if (l1->val < l2->val) {
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        } else {
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
};

int main(){
    vector<int> nums={2, 7, 11, 15};
    vector<int> nums2={2, 7, 11, 15};
    ListNode *t=create(nums);
    ListNode *t2=create(nums);
    print(t);
    Solution test;
    ListNode* t3=test.mergeTwoLists(t,t2);
    print(t3);
}
