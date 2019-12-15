# Runtime: 36 ms, faster than 94.70% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.

class Solution:
    def deleteDuplicates(self, head):

        if not head:
            return head
        def traverse(head):

            if head.next:
                traverse(head.next)

            if head.next and head.val == head.next.val:
                head.next = head.next.next

        traverse(head)
        return head
