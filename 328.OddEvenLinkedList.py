# Runtime: 40 ms, faster than 83.06% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Odd Even Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        prev = None
        dummy = ListNode(0)
        dummy.next = head
        R = ListNode(0)
        rep = R
        while head:
            prev = head.next
            if head.next:
                head.next = head.next.next
            rep.next = prev
            rep = rep.next
            if not head.next:
                head.next = R.next
                break
            head = head.next
        return dummy.next
