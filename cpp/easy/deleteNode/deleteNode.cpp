//
// Created by pro on 2019/11/19.
//
#include <vector>
#include <stdlib.h>
#include <iostream>

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