'''
https://github.com/baseballcoder1/LeetCode

LeetCode 328: Odd Even Linked List

Difficulty: Medium
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        odd = head
        oddstart = odd
        even = None
        evenstart = None
        x = head
        i = 0
        while x.next is not None:
            x = x.next
            if i % 2 == 1:
                odd.next = x
                odd = odd.next
            else:
                if even is None:
                    even = x
                    evenstart = even
                else:
                    even.next = x
                    even = even.next
            i += 1
        if evenstart is not None:
            odd.next = evenstart
            even.next = None
        else:
            odd.next = None
        return oddstart
