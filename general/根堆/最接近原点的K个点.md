## 每日一题 - 最接近原点的 K 个点
### 信息卡片 

- 时间： 2020-11-09
- 题目链接：https://leetcode-cn.com/problems/k-closest-points-to-origin/
- tag：根堆
- 题目描述：

我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。


示例 1：

    输入：points = [[1,3],[-2,2]], K = 1
    输出：[[-2,2]]
    解释： 
    (1, 3) 和原点之间的距离为 sqrt(10)，
    (-2, 2) 和原点之间的距离为 sqrt(8)，
    由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
    我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。

示例 2：

    输入：points = [[3,3],[5,-1],[-2,4]], K = 2
    输出：[[3,3],[-2,4]]
    （答案 [[-2,4],[3,3]] 也会被接受。）




### 参考答案

修改sort排序方法
```java
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        Arrays.sort(points, new Comparator<int[]>() {
            public int compare(int[] point1, int[] point2) {
                return (point1[0] * point1[0] + point1[1] * point1[1]) - (point2[0] * point2[0] + point2[1] * point2[1]);
            }
        });
        return Arrays.copyOfRange(points, 0, K);
    }
}
```
使用大根堆，每遇到比堆顶小的元素，栈出堆顶，栈入比堆顶小的元素。
```java
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> queue = new PriorityQueue<int[]>(new Comparator<int[]>() {
            public int compare(int[] arr1, int[] arr2) {
                return (arr2[0] * arr2[0] + arr2[1] * arr2[1])-(arr1[0] * arr1[0] + arr1[1] * arr1[1]);
            }
        });
        for (int i=0;i<points.length;i++){
            if (queue.size()>=K){
                int []tmp=queue.peek();
                int dist=tmp[0] * tmp[0]+tmp[1] * tmp[1];
                if (points[i][0]*points[i][0]+points[i][1]*points[i][1]<dist){
                    queue.poll();
                    queue.offer(points[i]);
                }
            }else{
                queue.offer(points[i]);
            }
        }
        int [][]ret=new int[K][2];
        for (int i=0;i<K;i++){
            ret[i]=queue.poll();
        }
        return ret;
    }
}
```

### 扩展

### 其他优秀解答 





