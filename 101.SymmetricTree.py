# Runtime: 24 ms, faster than 99.28% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def traverse(root):

            if any(root):
                L = len(root)
                queue = []
                nxt = []
                for v in root:
                    if v:
                        queue.append(v.val)
                        nxt.extend([v.left, v.right])
                    else:
                        queue.append(None)
                        nxt.append(None)

                if queue[: sum(divmod(L,2))] != queue[L // 2:][::-1]:
                #if queue != queue[::-1]:
                    print(queue)
                    return False

                else:
                    return traverse(nxt)
            return True
        return traverse([root])
