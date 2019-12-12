# Runtime: 40 ms, faster than 92.73% of Python3 online submissions for Path Sum.
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Path Sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        def traverse(root,target):

            if not root:
                return target == 0

            if root.left and root.right:
                return traverse(root.left,target - root.val) or traverse(root.right,target - root.val)
            elif root.left:
                return traverse(root.left,target - root.val)
            else:
                return traverse(root.right,target - root.val)
        return traverse(root,sum)
