"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        count = 0
        res = 0
        res = self.dfs(root,count,res)
        return res

        #return count

    def dfs(self,node,count,res):

        if not node.children:
            return count + 1

        tmp = []
        for child in node.children:
            #count += 1
            tmp.append(self.dfs(child,count + 1,[]))
            res = max(tmp)
        return res
