'''
https://github.com/baseballcoder1/LeetCode

LeetCode 25: Reverse Nodes in k-Group

Difficulty: Hard
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        x = head
        y = None
        while True:
            z = x
            a = [z]
            for i in range(k-1):
                if z.next is None:
                    break
                z = z.next
                a.append(z)
            znext = z.next
            if len(a) < k:
                y.next = x
                break
            for el in a[::-1]:
                if y is None:
                    y = el
                    result = y
                else:
                    y.next = el
                    y = y.next
            if znext is None:
                y.next = None
                break
            x = znext
        return result
