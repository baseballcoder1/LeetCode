'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1372: Longest ZigZag Path in a Binary Tree

Difficulty: Medium
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if node.left is None and node.right is None:
                return 0, 0, 0
            else:
                running = 0
                if node.left is None:
                    left = 0
                else:
                    x, y, z = traverse(node.left)
                    left = 1+y
                    running = max(running, z)
                if node.right is None:
                    right = 0
                else:
                    x, y, z = traverse(node.right)
                    right = 1+x
                    running = max(running, z)
                running = max(running, left, right)
                return left, right, running

        if root is None:
            return 0
        _, _, result = traverse(root)
        return result
