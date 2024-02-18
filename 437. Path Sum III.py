'''
https://github.com/baseballcoder1/LeetCode

LeetCode 437: Path Sum III

Difficulty: Medium
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traverse(node):
            totalsums = {}
            totalnum = 0
            for child in node.left, node.right:
                if child is None:
                    continue
                sums, num = traverse(child)
                for x in sums.keys():
                    if x not in totalsums:
                        totalsums[x] = sums[x]
                    else:
                        totalsums[x] += sums[x]
                totalnum += num
            need = targetSum - node.val
            if need in totalsums:
                totalnum += totalsums[need]
            if node.val == targetSum:
                totalnum += 1
            newtotalsums = {}
            for x, freq in totalsums.items():
                newtotalsums[x+node.val] = freq
            totalsums = newtotalsums
            if node.val not in totalsums:
                totalsums[node.val] = 1
            else:
                totalsums[node.val] += 1
            return totalsums, totalnum

        if root is None:
            return 0
        _, result = traverse(root)
        return result
