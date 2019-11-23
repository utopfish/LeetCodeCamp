//
// Created by pro on 2019/11/23.
//
#include <stack>
#include "../../nodeBase.h"
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(!head||!head->next) return true;
        ListNode *slow=head;
        ListNode *fast=head;

        stack<int>s;
        s.push(head->val);
        while(fast->next&&fast->next->next)
        {
            slow=slow->next;
            fast=fast->next->next;
            s.push(slow->val);
        }

        if(!fast->next) s.pop();
        while(slow->next)
        {
            slow=slow->next;
            int tmp=s.top();
            s.pop();
            if(tmp!=slow->val)
                return false;
        }
        return true;
    }
};
int main(){
    vector<int> nums={2, 7, 11, 15};
    ListNode *t=create(nums);
    print(t);
    Solution test;
    bool re=test.isPalindrome(t);
    cout << re<<endl;
}