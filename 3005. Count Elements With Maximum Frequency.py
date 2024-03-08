'''
https://github.com/baseballcoder1/LeetCode

LeetCode 3005: Count Elements With Maximum Frequency

LeetCode Daily Question

Difficulty: Easy
'''

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {x: nums.count(x) for x in nums}
        a = max(d.values())
        return sum([x for x in d.values() if x == a])
        