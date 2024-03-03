'''
https://github.com/baseballcoder1/LeetCode

LeetCode 515: Find Largest Value in Each Tree Row

Difficulty: Medium
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        current = [root]
        result = [root.val]
        while True:
            new = []
            for node in current:
                for child in node.left, node.right:
                    if child is None:
                        continue
                    new.append(child)
            if len(new) == 0:
                break
            result.append(max([x.val for x in new]))
            current = new
        return result
