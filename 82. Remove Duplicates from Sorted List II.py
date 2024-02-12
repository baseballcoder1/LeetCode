'''
https://github.com/baseballcoder1/LeetCode

LeetCode 82: Remove Duplicates from Sorted List II

Difficulty: Medium
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        x = head
        y = head
        yfreq = 1
        z = None
        result = None
        while x.next is not None:
            x = x.next
            if x.val != y.val:
                if yfreq == 1:
                    if z is None:
                        z = y
                        result = z
                    else:
                        z.next = y
                        z = z.next
                y = x
                yfreq = 1
            else:
                yfreq += 1
        if yfreq == 1:
            if z is None:
                z = y
                result = z
            else:
                z.next = y
                z = z.next
        if z is not None:
            z.next = None
        return result
