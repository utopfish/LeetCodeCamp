//
// Created by pro on 2019/11/22.
//
using namespace std;
typedef struct ListNode {
    int val;
    struct ListNode *next;
}ListNode;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head){
            return nullptr;
        }
        ListNode* first = head;//始终指向原链表的首位元素
        ListNode* target = head->next;//始终指向即将要放到当前链表首元素之前的目标元素
        while(target != nullptr){
            first->next = target->next;
            ListNode* temp = target->next;
            target->next = head;
            head = target;
            target = temp;
        }
        return head;

    }
};

class Solution1{
public:
    ListNode* reverseList(ListNode* head) {
        if(!head){
            return nullptr;
        }
        return reverse(head, head, head->next);
    }

    ListNode* reverse(ListNode* head, ListNode* first, ListNode* target){
        if(!target){
            return head;
        }
        first->next = target->next;
        ListNode* temp = target->next;
        target->next = head;
        return reverse(target, first, temp);
    }
};