# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        if root == None:
            return 0

        def BFS(root,res):
            queue = []
            queue.append(root)

            while queue:

                c = queue.pop(0)
                if L <= c.val <= R:
                    res += c.val
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
            return res

        return BFS(root,0)
                
