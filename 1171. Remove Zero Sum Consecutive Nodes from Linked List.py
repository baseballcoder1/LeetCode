'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1171: Remove Zero Sum Consecutive Nodes from Linked List

LeetCode Daily Question

Difficulty: Medium
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        nodes = [head]
        current = head
        while current.next is not None:
            nodes.append(current.next)
            current = current.next
        while True:
            vals = [node.val for node in nodes]
            match = False
            for i in range(len(nodes)):
                if match:
                    break
                for j in range(i, len(nodes)):
                    if match:
                        break
                    if sum(vals[i:j+1]) == 0:
                        if i == 0:
                            if j+1 <= len(nodes)-1:
                                head = nodes[j+1]
                            else:
                                return None
                        else:
                            if j+1 <= len(nodes)-1:
                                nodes[i-1].next = nodes[j+1]
                            else:
                                nodes[i-1].next = None
                        del nodes[i:j+1]
                        match = True
            if not match:
                break
        return head
