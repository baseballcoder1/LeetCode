'''
https://github.com/baseballcoder1/LeetCode

LeetCode 129: Sum Root to Leaf Numbers

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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        def paths(node):
            if node.left is None and node.right is None:
                yield [node.val]
                return
            for child in node.left, node.right:
                if child is None:
                    continue
                for path in paths(child):
                    yield [node.val] + list(path)

        return sum(map(lambda x: int("".join(str(y) for y in x)), paths(root)))
