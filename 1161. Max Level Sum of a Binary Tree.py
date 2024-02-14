'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1161: Max Level Sum of a Binary Tree

Difficulty: Medium
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        nodes = [root]
        level = 1
        maxsum = root.val
        maxlevel = 1
        while True:
            total = sum([node.val for node in nodes])
            if total > maxsum:
                maxsum = total
                maxlevel = level
            newnodes = []
            for node in nodes:
                if node.left is None and node.right is None:
                    continue
                for child in node.left, node.right:
                    if child is None:
                        continue
                    newnodes.append(child)
            if len(newnodes) == 0:
                break
            nodes = newnodes
            level += 1
        return maxlevel
