'''
https://github.com/baseballcoder1/LeetCode

LeetCode 977: Squares of a Sorted Array

LeetCode Daily Question

Difficulty: Easy
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x*x for x in nums])
        