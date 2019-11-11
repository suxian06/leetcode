# Runtime: 32 ms, faster than 93.81% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        val = []

        def BFS(root,val):
            if root:
                val += [v.val for v in [root]]
            if root.left:
                BFS(root.left,val)
            if root.right:
                BFS(root.right,val)

        def BFS_reset(root,val):
            if root:
                root.val = val.pop(0)
            if root.left:
                BFS_reset(root.left,val)
            if root.right:
                BFS_reset(root.right,val)

        BFS(root,val)
        print(val)
        sum_val = [0]*len(val)
        for i in range(len(val)):
            sum_val[i] = sum([v for v in val if v >= val[i]])
        print(sum_val)
        BFS_reset(root,sum_val)

        return root
