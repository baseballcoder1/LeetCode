'''
https://github.com/baseballcoder1/LeetCode

LeetCode 513: Find Bottom Left Value Tree

LeetCode Daily Question

Difficulty: Medium
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        current = [root]
        while True:
            new = []
            for node in current:
                for child in node.left, node.right:
                    if child is None:
                        continue
                    new.append(child)
            if len(new) == 0:
                break
            current = new
        return current[0].val
        