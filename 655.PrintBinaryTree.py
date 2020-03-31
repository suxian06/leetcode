# Runtime: 24 ms, faster than 98.88% of Python3 online submissions for Print Binary Tree.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Print Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:


        def height(root):

            if root:
                return max(height(root.left),height(root.right)) + 1
            return 0

        h = height(root)
        c = sum(2**x for x in range(h))
        ans = [["" for i in range(c)] for j in range(h)]

        def traverse(root,level,p,h,ans):

            if root:
                ans[level][p] = str(root.val)

            if root.left:
                traverse(root.left,level + 1,p - 2**(h - 1),h - 1,ans)
            if root.right:
                traverse(root.right,level + 1,p + 2**(h - 1),h - 1,ans)

        traverse(root,0,c//2,h - 1,ans)
        return ans
