# Runtime: 100 ms, faster than 96.08% of Python3 online submissions for Linked List Components.
# Memory Usage: 17.4 MB, less than 75.00% of Python3 online submissions for Linked List Components.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    res = 0
    prev = False
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        self.res = 0
        self.prev = False
        setG = set(G)
        def traverse(head,prev):

            while head:
                if head.val in setG:
                    self.prev = True
                else:
                    if self.prev:
                        self.res += 1
                        self.prev = False
                head = head.next

        traverse(head,self.prev)

        if self.prev:
            return self.res + 1
        return self.res
