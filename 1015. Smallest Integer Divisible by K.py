'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1015: Smallest Integer Divisible by K

Difficulty: Medium
'''

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        elif k % 5 == 0:
            return -1
        else:
            x = 1
            y = 1
            while x % k != 0:
                x *= 10
                x += 1
                y += 1
            return y
