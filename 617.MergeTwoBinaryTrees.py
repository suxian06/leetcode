# Runtime: 80 ms, faster than 87.45% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 13.4 MB, less than 94.29% of Python3 online submissions for Merge Two Binary Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        #head = TreeNode(0)
        if not t1:
            return t2

        def traverse(t1,t2):

            if t1 and t2:
                t1.val = t1.val + t2.val
                if not t1.left and t2.left:
                    t1.left = TreeNode(0)
                traverse(t1.left, t2.left)
                if not t1.right and t2.right:
                    t1.right = TreeNode(0)
                traverse(t1.right, t2.right)

            elif t2:
                t1.val = t2.val


        traverse(t1, t2)
        return t1
