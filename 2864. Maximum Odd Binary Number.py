'''
https://github.com/baseballcoder1/LeetCode

LeetCode 2864: Maximum Odd Binary Number

LeetCode Daily Question

Difficulty: Easy
'''

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        x = len(s)
        y = s.count("1")
        return "1" * (y-1) + "0" * (x-y) + "1"
        