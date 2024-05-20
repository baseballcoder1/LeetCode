'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1863: Sum of All Subset XOR Totals

LeetCode Daily Question

Difficulty: Easy
'''

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        from itertools import combinations
        result = 0
        for i in range(1, len(nums)+1):
            for a in combinations(nums, i):
                x = 0
                for y in a:
                    x ^= y
                result += x
        return result
