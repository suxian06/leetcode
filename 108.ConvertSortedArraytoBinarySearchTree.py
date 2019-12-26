# Runtime: 52 ms, faster than 99.89% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        L = len(nums)
        if L == 0:
            return
        m = L // 2
        l, r = m - 1, L - 1
        def traverse(l,m,r):

            res = TreeNode(nums[m])

            if m > l :

                res.left = traverse(l,(l + m)// 2, m)
            if (m + r + 1) // 2 < r:

                res.right = traverse(m + 1, (m + r + 1) // 2,r)

            return res
        res = traverse(0,m,L)
        return res
