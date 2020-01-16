# Runtime: 104 ms, faster than 61.38% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def traverse(root):

            if not root:
                return 0

            ans = traverse(root.left) + traverse(root.right)
            if root.val % 2 == 0:
                self.ans += ans

            if root.left and root.right:
                return root.left.val + root.right.val

            elif root.left:
                return root.left.val
            elif root.right:
                return root.right.val
            else:
                return 0

        traverse(root)
        return self.ans
