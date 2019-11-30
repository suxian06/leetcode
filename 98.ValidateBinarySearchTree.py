# Runtime: 36 ms, faster than 98.85% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 15.0 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = True
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def traverse(root,low,high):
            if self.res:
                if not root:
                    return

                elif low < root.val < high:
                    traverse(root.left,low,root.val)
                    traverse(root.right,root.val,high)
                else:
                    self.res = False

        traverse(root,float("-inf"),float("inf"))
        return self.res
