# Runtime: 28 ms, faster than 96.19% of Python3 online submissions for Binary Tree Pruning.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Pruning.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    remove = False
    def pruneTree(self, root: TreeNode) -> TreeNode:
        h = root
        if not root:
            return root
        def traverse(root):
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)

            if root.right and root.right.val == 0:
                if root.right.left or root.right.right:
                    pass
                else:
                    root.right = None

            if root.left and root.left.val == 0:
                if root.left.right or root.left.left:
                    pass
                else:
                    root.left = None

        traverse(root)

        return h
