//
// Created by pro on 2019/11/24.
//
#include "../../nodeBase.h"
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head==NULL||head->next==NULL)
            return false;
        ListNode *k=head;//检测节点
        ListNode *q=head->next;//遍历节点
        int count=0;//记录检测节点走了多少步
        while(q)
        {
            for(int i=count;i>0;i--)
            {
                k=k->next;
                if(k==q)
                    return true;
            }
            k=head;//还原
            q=q->next;
            count++;
        }
        return false;
    }
};
int main(){
    vector<int> nums={2, 7, 11, 15};
    ListNode *t=create(nums);
   
    print(t);
}