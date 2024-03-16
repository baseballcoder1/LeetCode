'''
https://github.com/baseballcoder1/LeetCode

LeetCode 525: Contiguous Array

LeetCode Daily Question

Difficulty: Medium
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        x = 0
        d = {0: [0]}
        for i, num in enumerate(nums):
            if num == 0:
                x -= 1
            else:
                x += 1
            if x not in d:
                d[x] = []
            d[x].append(i+1)
        result = 0
        for x in d.keys():
            a = d[x]
            result = max(result, a[-1]-a[0])
        return result
