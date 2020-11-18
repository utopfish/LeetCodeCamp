## 每日一题 - 删除链表的倒数第N个节点
### 信息卡片 

- 时间： 2020-10-18
- 题目链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
- tag：链表，双指针
- 题目描述：

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

    给定一个链表: 1->2->3->4->5, 和 n = 2.

    当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？



### 参考答案

一次遍历双指针
c++
```c++
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
             ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;

        ListNode* p = dummyHead;
        ListNode* q = dummyHead;
        for( int i = 0 ; i < n + 1 ; i ++ ){
            q = q->next;
        }

        while(q){
            p = p->next;
            q = q->next;
        }
        ListNode* delNode = p->next;
        p->next = delNode->next;
        delete delNode;
        ListNode* retNode = dummyHead->next;
        delete dummyHead;
        return retNode;
    }
};

```
python
```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode(0,head)
        fir=dummy
        sec=head

        for i in range(n):
            sec=sec.next
        
        while sec:
            sec=sec.next
            fir=fir.next
        fir.next=fir.next.next
        return dummy.next

```
js
```js
var removeNthFromEnd = function(head, n) {
    let dummy=new ListNode(0)
    dummy.next=head
    let fir=dummy
    let sec=dummy.next
    for (let i=0;i<n;i++){
        sec=sec.next
    }
    while(sec){
        sec=sec.next
        fir=fir.next
    }
    fir.next=fir.next.next
    return dummy.next
};

```
java
```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy=new ListNode(0,head);
        ListNode fir=dummy;
        ListNode sec=fir.next;
        for(int i=0;i<n;i++){
            sec=sec.next;
        }
        while(sec!=null){
            fir=fir.next;
            sec=sec.next;
        }
        fir.next=fir.next.next;
        return dummy.next;
    }
}
```

### 扩展

### 其他优秀解答 





