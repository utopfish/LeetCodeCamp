class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res=[]
        def find(root,path,score):
            if not root:
                return
            if not root.left and root.right:
                if score+root.val==sum:
                    res.append(path)
                return
            if score+root.val>sum:
                return
            find(root.left, path+[root.val], score+root.val)
            find(root.right, path+[root.val], score+root.val)
            return
        find(root, [], 0)
        return res