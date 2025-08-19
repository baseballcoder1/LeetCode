'''
https://github.com/baseballcoder1/LeetCode

LeetCode 2348: Number of Zero-Filled Subarrays

LeetCode Daily Question

Difficulty: Medium
'''

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        x = 0
        y = 0
        for z in nums:
            if z == 0:
                y += 1
            else:
                if y > 0:
                    x += y*(y+1)//2
                    y = 0
        if y > 0:
            x += y*(y+1)//2
        return x
