'''
https://github.com/baseballcoder1/LeetCode

LeetCode 7: Reverse Integer

Difficulty: Medium
'''

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] != "-":
            xrev = int(s[::-1])
        else:
            xrev = -int(s[-1:0:-1])
        if xrev < -(2**31) or xrev > 2**31 - 1:
            return 0
        return xrev
