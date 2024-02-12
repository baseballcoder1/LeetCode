'''
https://github.com/baseballcoder1/LeetCode

LeetCode 19: Remove Nth Node From End of List

Difficulty: Medium
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = head
        i = 0
        while l.next is not None:
            l = l.next
            i += 1
        j = i-n+1
        prev = None
        now = head
        for k in range(j):
            prev, now = now, now.next
        if j == 0:
            head = head.next
        else:
            prev.next = now.next
        return head
