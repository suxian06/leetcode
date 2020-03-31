# Runtime: 28 ms, faster than 99.84% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List II.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #h = ListNode(0)
        #h.next = head
        c = 1
        d = ListNode(0)
        d.next = head
        p = d
        while head:

            if not head.next and c > 1:
                p.next = None
                break
            if head.next and head.val == head.next.val:
                c += 1
                head = head.next
            else:
                if c > 1:
                    c = 1
                    head = head.next
                else:
                    c = 1
                    p.next = head
                    p = p.next
                    head = head.next

        return d.next
