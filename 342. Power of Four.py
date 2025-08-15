'''
https://github.com/baseballcoder1/LeetCode

LeetCode 342: Power of Four

LeetCode Daily Question

Difficulty: Easy
'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        for i in range(n+1):
            x = 4**i
            if x == n:
                return True
            if x > n:
                break
        return False
