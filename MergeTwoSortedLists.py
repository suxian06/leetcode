class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        s = ListNode(0)
        l = s
        while (l1 != None) & (l2 != None):

            a = l1.val
            b = l2.val

            if a > b:
                l.next = l2
                l = l.next
                l2 = l2.next
            else:
                l.next = l1
                l = l.next
                l1 = l1.next

        l.next = l1 or l2
        l = s.next
        return l
