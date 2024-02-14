'''
https://github.com/baseballcoder1/LeetCode

LeetCode 238: Product of Array Except Self

Difficulty: Medium
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod1 = []
        x = 1
        for y in nums[:-1]:
            x *= y
            prod1 += [x]
        prod2 = []
        x = 1
        for y in nums[-1:0:-1]:
            x *= y
            prod2 += [x]
        result = []
        for i in range(len(nums)):
            if i == 0:
                x = 1
            else:
                x = prod1[i-1]
            j = len(nums)-1-i
            if j == 0:
                y = 1
            else:
                y = prod2[j-1]
            result += [x*y]
        return result
