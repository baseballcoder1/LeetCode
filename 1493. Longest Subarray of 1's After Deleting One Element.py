'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1493: Longest Subarray of 1's After Deleting One Element

Difficulty: Medium
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        start = 0
        numones = 0
        d = {}
        for i, num in enumerate(nums):
            if numones == 0:
                if num == 1:
                    start = i
                    numones = 1
            else:
                if num == 1:
                    numones += 1
                else:
                    d[start] = numones
                    numones = 0
        if numones >= 1:
            d[start] = numones
        i = sorted(d.keys())
        maxones = 0
        if 0 in nums:
            maxones = max(maxones, max(d.values(), default=0))
        else:
            return len(nums)-1
        for j in i[:-1]:
            if j + d[j] + 1 in d:
                maxones = max(maxones, d[j] + d[j + d[j] + 1])
        return maxones
