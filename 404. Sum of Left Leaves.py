'''
https://github.com/baseballcoder1/LeetCode

LeetCode 404: Sum of Left Leaves

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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def leftleaf(node):
            if node.left is not None:
                if node.left.left is None and node.left.right is None:
                    yield node.left.val
            for child in node.left, node.right:
                if child is not None:
                    yield from leftleaf(child)

        return sum(leftleaf(root))
