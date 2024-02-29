'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1609: Even Odd Tree

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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        current = [root]
        level = 0
        if root.val % 2 != 1:
            return False
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
            level += 1
            val = [node.val for node in current]
            if level % 2 == 1:
                x = val[0]
                if x % 2 != 0:
                    return False
                for y in val[1:]:
                    if y % 2 != 0:
                        return False
                    if not y < x:
                        return False
                    x = y
            else:
                x = val[0]
                if x % 2 != 1:
                    return False
                for y in val[1:]:
                    if y % 2 != 1:
                        return False
                    if not y > x:
                        return False
                    x = y
        return True
