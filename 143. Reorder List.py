'''
https://github.com/baseballcoder1/LeetCode

LeetCode 143: Reorder List

LeetCode Daily Question

Difficulty: Medium
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = [head]
        node = head
        while node.next is not None:
            node = node.next
            nodes.append(node)
        node = head
        for i in range(len(nodes)//2):
            nextnode = node.next
            endnode = nodes.pop()
            node.next = endnode
            endnode.next = nextnode
            node = nextnode
        node.next = None
        