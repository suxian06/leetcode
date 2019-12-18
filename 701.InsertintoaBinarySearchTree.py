# Runtime: 108 ms, faster than 98.24% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Insert into a Binary Search Tree.
class Solution:
    def insertIntoBST(self, root, val):

        if not root:
            return TreeNode(val)

        def traverse(root):

            if root:

                if root.val < val:
                    if root.right:
                        traverse(root.right)
                    else:
                        root.right = TreeNode(val)

                else:
                    if root.left:
                        traverse(root.left)
                    else:
                        root.left = TreeNode(val)
        traverse(root)
        return root
