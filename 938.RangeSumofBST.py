# Runtime: 268 ms, faster than 45.43% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 20.7 MB, less than 100.00% of Python3 online submissions for Range Sum of BST.


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
            import collections
            queue = collections.deque()
            queue.append(root)

            while queue:

                c = queue.popleft()
                if L <= c.val <= R:
                    res += c.val
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
            return res

        return BFS(root,0)
