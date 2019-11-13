# Runtime: 344 ms, faster than 54.38% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
# Memory Usage: 17.2 MB, less than 100.00% of Python3 online submissions for Maximum Level Sum of a Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        def BFS(root):

            import collections
            queue = collections.deque()
            queue.append(root)
            level = 1
            curLevel = 0
            curSum = 0
            maxSum = -1000000
            count = 0
            while queue:

                curSum = sum([c.val for c in queue if c != None])
                if curSum > maxSum:
                    curLevel = level
                    maxSum = curSum
                #print(curSum)
                queue = [c.left for c in queue if c != None] + [c.right for c in queue if c != None]
                level += 1
            return curLevel

        return BFS(root)
