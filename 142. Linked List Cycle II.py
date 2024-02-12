'''
https://github.com/baseballcoder1/LeetCode

LeetCode 142: Linked List Cycle II

Difficulty: Medium
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        x = head
        d = {x: 1}
        while x.next is not None:
            if x.next in d:
                return x.next
            x = x.next
            d[x] = 1
        return None
