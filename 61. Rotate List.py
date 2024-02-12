'''
https://github.com/baseballcoder1/LeetCode

LeetCode 61: Rotate List

Difficulty: Medium
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        node = head
        nodes = []
        nodes.append(node)
        while node.next is not None:
            node = node.next
            nodes.append(node)
        numnodes = len(nodes)
        i = numnodes - (k % numnodes)
        i %= numnodes
        result = nodes[i]
        for j in range(numnodes-1):
            nodes[i % numnodes].next = nodes[(i + 1) % numnodes]
            i += 1
        nodes[i % numnodes].next = None
        return result
