# Runtime: 40 ms, faster than 42.55% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head:
            return None
        newList = ListNode(0)
        newListHead = newList
        c = -1
        while head.next:
            c = 0
            h = head
            n = head.next
            newList.val = n.val
            newList.next = ListNode(h.val)
            newList = newList.next
            while c < 2 and head.next:
                head = head.next
                c += 1
            if c == 2:
                newList.next = ListNode(0)
                newList = newList.next

        if c != 1:
            newList.val = head.val

        return newListHead
