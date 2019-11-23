# Runtime: 28 ms, faster than 98.74% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 18.6 MB, less than 22.73% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# recursive solution
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        def traverse(head,prev):
            if head.next:
                nxt = head.next
                head.next = prev
                prev = head
                return traverse(nxt,prev)
            else:
                head.next = prev
                return head

        return traverse(head,None)

# Runtime: 36 ms, faster than 87.68% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# iterative solution
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = None
        while head.next:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        head.next = cur
        return head
