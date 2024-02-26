'''
https://github.com/baseballcoder1/LeetCode

LeetCode 100: Same Tree

LeetCode Daily Question

Difficulty: Easy
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node):
            if node.left is not None:
                for pos, val in traverse(node.left):
                    yield "0" + pos, val
            yield "", node.val
            if node.right is not None:
                for pos, val in traverse(node.right):
                    yield "1" + pos, val
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        return list(traverse(p)) == list(traverse(q))
