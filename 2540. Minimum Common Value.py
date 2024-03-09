'''
https://github.com/baseballcoder1/LeetCode

LeetCode 2540: Minimum Common Value

LeetCode Daily Question

Difficulty: Easy
'''

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1) & set(nums2), default=-1)
        