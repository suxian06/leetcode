# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        return self.dfs(root,1)


    def dfs(self,node,depth):

        if node.left and node.right:
            val = max(self.dfs(node.left,depth + 1),self.dfs(node.right,depth + 1))

        elif node.left:
            val = self.dfs(node.left,depth + 1)
        elif node.right:
            val = self.dfs(node.right,depth + 1)
        else:
            val = depth
        return val
