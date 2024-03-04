'''
https://github.com/baseballcoder1/LeetCode

LeetCode 2265: Count Nodes Equal to Average of Subtree

Difficulty: Medium
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def traverse(node):
            if node.left is None and node.right is None:
                return 1, [node.val]
            else:
                result = 0
                vals = [node.val]
                for child in node.left, node.right:
                    if child is None:
                        continue
                    x, l = traverse(child)
                    result += x
                    vals += l
                if node.val == sum(vals)//len(vals):
                    result += 1
                return result, vals

        result, _ = traverse(root)
        return result
