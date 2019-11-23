//
// Created by pro on 2019/11/23.
//

#ifndef CPP_NODEBASE_H
#define CPP_NODEBASE_H

#endif //CPP_NODEBASE_H
#include <stdlib.h>
#include <iostream>
#include <vector>
using namespace std;
typedef struct ListNode {
    int val;
    struct ListNode *next;
}ListNode;
ListNode* create(vector<int> nums){
    ListNode *p,*head;
    head=new ListNode;
    p=head;
    for (int i=0;i<nums.size();i++){
        ListNode *s = new ListNode;//声明List对象来保存数据  这就是一个链表的节点
        s->val = nums[i];//将数据保存到此节点
        p->next = s;//将此节点与头节点连接
        p = s;
    };
    head = head->next;
    p->next = NULL;
    return head;

};
void print(ListNode *head) {//打印输出链表
    ListNode *p = head;
    while (p != NULL) {
        cout << to_string(p->val)+" ";
        p = p->next;
    }
    cout<<""<<endl;
}