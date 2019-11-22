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

# Runtime: 28 ms, faster than 94.87% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.
# Nice recursive solution learned from leetcode explore and discussion
# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second
