'''
https://github.com/baseballcoder1/LeetCode

LeetCode 78: Subsets

LeetCode Daily Question

Difficulty: Medium
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(pow(2, n)):
            s = bin(i)[2:]
            if len(s) < n:
                s = '0' * (n-len(s)) + s
            a = [nums[j] for j in range(n) if s[j] == '1']
            result.append(a)
        return result
