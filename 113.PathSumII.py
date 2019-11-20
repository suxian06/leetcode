# Runtime: 44 ms, faster than 94.75% of Python3 online submissions for Path Sum II.
# Memory Usage: 17.7 MB, less than 37.93% of Python3 online submissions for Path Sum II.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #res = []
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return []
        def traverse(root,s,path,res):
            if root.left:
                traverse(root.left,s + root.val,path + [root.val],res)
            if root.right:
                traverse(root.right,s + root.val,path + [root.val],res)

            if not root.right and not root.left and s + root.val == sum:
                res.append(path + [root.val])

        traverse(root,0,[],res)
        return res
