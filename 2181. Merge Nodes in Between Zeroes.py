'''
https://github.com/baseballcoder1/LeetCode

LeetCode 2181: Merge Nodes in Between Zeroes

LeetCode Daily Question

Difficulty: Medium
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = None
        c = None
        d = 0
        while True:
            if a.val != 0:
                if d == 0:
                    c = a
                d += a.val
            else:
                if c is None:
                    a = a.next
                    continue
                if b is None:
                    result = c
                else:
                    b.next = c
                c.val = d
                b = c
                d = 0
                if a.next is None:
                    c.next = None
                    break
            a = a.next
        return result
