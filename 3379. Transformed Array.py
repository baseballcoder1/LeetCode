'''
https://github.com/baseballcoder1/LeetCode

LeetCode 3379: Transformed Array

LeetCode Daily Question

Difficulty: Easy
'''

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        for x in nums:
            if x < 0:
                j = i - (abs(x) % len(nums))
                if j < 0:
                    j += len(nums)
            elif x == 0:
                j = i
            else:
                j = i + x
                j %= len(nums)
            result.append(nums[j])
            i += 1
        return result
