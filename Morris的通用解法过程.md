## Morris的通用解法过程
[![BQ9lhn.png](https://s1.ax1x.com/2020/10/27/BQ9lhn.png)](https://imgchr.com/i/BQ9lhn)

Morris的整体思路就是将 以某个根结点开始，找到它左子树的最右侧节点之后与这个根结点进行连接。
我们可以从 图2 看到，如果这么连接之后，cur 这个指针是可以完整的从一个节点顺着下一个节点遍历，将整棵树遍历完毕，直到 7 这个节点右侧没有指向。
```java
public static void preOrderMorris(TreeNode head) {
	if (head == null) {
		return;
	}
	TreeNode cur1 = head;//当前开始遍历的节点
	TreeNode cur2 = null;//记录当前结点的左子树
	while (cur1 != null) {
		cur2 = cur1.left;
		if (cur2 != null) {
			while (cur2.right != null && cur2.right != cur1) {//找到当前左子树的最右侧节点，且这个节点应该在指向根结点之前，否则整个节点又回到了根结点。
				cur2 = cur2.right;
			}
			if (cur2.right == null) {//这个时候如果最右侧这个节点的右指针没有指向根结点，创建连接然后往下一个左子树的根结点进行连接操作。
				cur2.right = cur1;
				cur1 = cur1.left;
				continue;
			} else {//当左子树的最右侧节点有指向根结点，此时说明我们已经回到了根结点并重复了之前的操作，同时在回到根结点的时候我们应该已经处理完 左子树的最右侧节点 了，把路断开。
				cur2.right = null;
			}
		} 
		cur1 = cur1.right;//一直往右边走，参考图
	}
}
```

[[前序遍历]]


1. 在某个根结点创建连线的时候打印。因为我们是顺着左边的根节点来创建连线，且创建的过程只有一次。

2. 打印某些自身无法创建连线的节点，也就是叶子节点。

```java
public static void preOrderMorris(TreeNode head) {
	if (head == null) {
		return;
	}
	TreeNode cur1 = head;
	TreeNode cur2 = null;
	while (cur1 != null) {
		cur2 = cur1.left;
		if (cur2 != null) {
			while (cur2.right != null && cur2.right != cur1) {
				cur2 = cur2.right;
			}
			if (cur2.right == null) {
				cur2.right = cur1;
				System.out.print(cur1.value + " ");
				cur1 = cur1.left;
				continue;
			} else {
				cur2.right = null;
			}
		} else {
			System.out.print(cur1.value + " ");
		}
		cur1 = cur1.right;
	}
}
```
[[中序遍历]]
从最左侧开始顺着右节点打印。也就是在将cu1切换到上层节点的时候。

```java
public static void inOrderMorris(TreeNode head) {
	if (head == null) {
		return;
	}
	TreeNode cur1 = head;
	TreeNode cur2 = null;
	while (cur1 != null) {
		cur2 = cur1.left;
		//构建连接线
		if (cur2 != null) {
			while (cur2.right != null && cur2.right != cur1) {
				cur2 = cur2.right;
			}
			if (cur2.right == null) {
				cur2.right = cur1;
				cur1 = cur1.left;
				continue;
			} else {
				cur2.right = null;
			}
		}
		System.out.print(cur1.value + " ");
		cur1 = cur1.right;
	}
}
```

[[后续遍历]]
[![BQCzIH.png](https://s1.ax1x.com/2020/10/27/BQCzIH.png)](https://imgchr.com/i/BQCzIH)

当我们到达最左侧，也就是左边连线已经创建完毕了。
打印 4
打印 5 2
打印 6
打印 7 3 1
我们将一个节点的连续右节点当成一个单链表来看待。
当我们返回上层之后，也就是将连线断开的时候，打印下层的单链表。
比如返回到　２，此时打印　４
比如返回到　１，此时打印　５　２
比如返回到　３，此时打印　６
那么我们只需要将这个单链表逆序打印就行了，下文也给出了 单链表逆序代码
这里不应该打印当前层，而是下一层，否则根结点会先与右边打印。

```java
//后序Morris
public static void postOrderMorris(TreeNode head) {
	if (head == null) {
		return;
	}
	TreeNode cur1 = head;//遍历树的指针变量
	TreeNode cur2 = null;//当前子树的最右节点
	while (cur1 != null) {
		cur2 = cur1.left;
		if (cur2 != null) {
			while (cur2.right != null && cur2.right != cur1) {
				cur2 = cur2.right;
			}
			if (cur2.right == null) {
				cur2.right = cur1;
				cur1 = cur1.left;
				continue;
			} else {
				cur2.right = null;
				postMorrisPrint(cur1.left);
			}
		}
		cur1 = cur1.right;
	}
	postMorrisPrint(head);
}
//打印函数
public static void postMorrisPrint(TreeNode head) {
	TreeNode reverseList = postMorrisReverseList(head);
	TreeNode cur = reverseList;
	while (cur != null) {
		System.out.print(cur.value + " ");
		cur = cur.right;
	}
	postMorrisReverseList(reverseList);
}
//翻转单链表
public static TreeNode postMorrisReverseList(TreeNode head) {
	TreeNode cur = head;
	TreeNode pre = null;
	while (cur != null) {
		TreeNode next = cur.right;
		cur.right = pre;
		pre = cur;
		cur = next;
	}
	return pre;
}
```