# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = ListNode(0)
        ans = prev
        tmp = 0
        while l1 and l2:
            v1 = l1.val
            v2 = l2.val
            l1 = l1.next
            l2 = l2.next
            if v1 + v2 + tmp < 10:
                ans.next = ListNode(v1 + v2 + tmp)
                ans = ans.next
                tmp = 0
            else:
                ans.next = ListNode(v1 + v2 + tmp - 10)
                ans = ans.next
                tmp = 1

        while l1:
            v1 = l1.val
            l1 = l1.next
            if v1 + tmp < 10:
                ans.next = ListNode(v1 + tmp)
                ans = ans.next
                tmp = 0
            else:
                ans.next = ListNode(v1 + tmp - 10)
                ans = ans.next
                tmp = 1

        while l2:
            v2 = l2.val
            l2 = l2.next
            if v2 + tmp < 10:
                ans.next = ListNode(v2 + tmp)
                ans = ans.next
                tmp = 0
            else:
                ans.next = ListNode(v2 + tmp - 10)
                ans = ans.next
                tmp = 1

        if tmp != 0:
            ans.next = ListNode(tmp)

        return prev.next
            
