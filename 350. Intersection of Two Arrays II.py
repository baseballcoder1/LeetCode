'''
https://github.com/baseballcoder1/LeetCode

LeetCode 350. Intersection of Two Arrays II

LeetCode Daily Question

Difficulty: Easy
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        for num in nums1:
            if num not in d1:
                d1[num] = 1
            else:
                d1[num] += 1
        d2 = {}
        for num in nums2:
            if num not in d2:
                d2[num] = 1
            else:
                d2[num] += 1
        result = []
        for num in d1.keys():
            if num in d2:
                x = min(d1[num], d2[num])
                result += [num] * x
        return result
