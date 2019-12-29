# Runtime: 28 ms, faster than 81.26% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Invert Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def traverse(root):
            if root:
                root.left, root.right = root.right, root.left
                traverse(root.left)
                traverse(root.right)

        traverse(root)
        return root
