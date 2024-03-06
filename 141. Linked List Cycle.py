'''
https://github.com/baseballcoder1/LeetCode

LeetCode 141: Linked List Cycle

LeetCode Daily Question

Difficulty: Easy
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        current = head
        seen = {current}
        while current.next is not None:
            current = current.next
            if current in seen:
                return True
            seen.update({current})
        return False
