'''
https://github.com/baseballcoder1/LeetCode

LeetCode 2: Add Two Numbers

Difficulty: Medium
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        now1 = l1
        now2 = l2
        carry = 0
        l = None
        while True:
            if now1 is None and now2 is None:
                break
            x = 0
            if now1 is not None:
                x += now1.val
                now1 = now1.next
            if now2 is not None:
                x += now2.val
                now2 = now2.next
            x += carry
            if l is None:
                l = ListNode(x % 10)
                result = l
            else:
                l.next = ListNode(x % 10)
                l = l.next
            carry = x // 10
        while carry > 0:
            l.next = ListNode(carry % 10)
            l = l.next
            carry //= 10
        return result
