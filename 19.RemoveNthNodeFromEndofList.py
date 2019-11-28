# Runtime: 28 ms, faster than 97.78% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    i = 0
    node = None
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        h = head

        def traverse(head):

            if head.next:
                traverse(head.next)
            self.i += 1
            if self.i == n - 1:
                self.node = head

            if self.i == n + 1:
                head.next = self.node
        traverse(head)
        if self.i == n:
            return h.next
        return h
