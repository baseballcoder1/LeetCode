'''
https://github.com/baseballcoder1/LeetCode

LeetCode 876: Middle of the Linked List

LeetCode Daily Question

Difficulty: Easy
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        nodes = [head]
        now = head
        while True:
            if now.next is None:
                break
            now = now.next
            nodes.append(now)
        return nodes[len(nodes)//2]
        