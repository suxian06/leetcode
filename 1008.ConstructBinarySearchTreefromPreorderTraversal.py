# Runtime: 24 ms, faster than 99.43% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
# inspired by Lee's code here https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252232/JavaC%2B%2BPython-O(N)-Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    index = 0
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        self.index = 0
        L = len(preorder)

        def BuildTree(preorder, limit, L):
            root = None
            if self.index < L and preorder[self.index] < limit:
                root = TreeNode(preorder[self.index])
                self.index += 1
                if self.index < L:
                    root.left = BuildTree(preorder, root.val, L)
                    root.right = BuildTree(preorder, limit, L)
            return root
        return BuildTree(preorder,float('inf'),L)
