# Runtime: 24 ms, faster than 89.10% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        c = ""
        if not head:
            return 0
        while True:
            c += str(head.val)
            if head.next:
                head = head.next
            else:
                break
        return int(c,base = 2)
