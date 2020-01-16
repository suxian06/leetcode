# Runtime: 352 ms, faster than 68.11% of Python3 online submissions for All Elements in Two Binary Search Trees.
# Memory Usage: 20.5 MB, less than 100.00% of Python3 online submissions for All Elements in Two Binary Search Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    l1,l2 = [], []
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.l1, self.l2 = [], []
        def Traverse(root,l):
            if root:
                Traverse(root.left,l)
                l.append(root.val)
                Traverse(root.right,l)

        Traverse(root1,self.l1)
        Traverse(root2,self.l2)

        def MergeSort(l1,l2):
            L1,L2 = len(l1), len(l2)
            i,j,seq = 0 , 0, []
            while i < L1 and j < L2:
                if l1[i] < l2[j]:
                    seq.append(l1[i])
                    i += 1
                else:
                    seq.append(l2[j])
                    j += 1

            if i < L1:
                seq += l1[i:]
            elif j < L2:
                seq += l2[j:]
            return seq

        return MergeSort(self.l1, self.l2)
