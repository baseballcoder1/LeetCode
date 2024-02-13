'''
https://github.com/baseballcoder1/LeetCode

LeetCode 113: Path Sum II

Difficulty: Medium
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
            
        def paths(node):
            if node.left is None and node.right is None:
                yield [node.val]
                return
            for child in node.left, node.right:
                if child is None:
                    continue
                for path in paths(child):
                    yield [node.val] + list(path)

        return list(filter(lambda x: sum(x) == targetSum, paths(root)))
