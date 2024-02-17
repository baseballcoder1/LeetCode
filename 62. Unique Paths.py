'''
https://github.com/baseballcoder1/LeetCode

LeetCode 62: Unique Paths

Difficulty: Medium
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def choose(n, r):
            def factorial(n):
                if n == 0:
                    return 1
                else:
                    return n*factorial(n-1)
            result = 1
            for i in range(n-r+1, n+1):
                result *= i
            result //= factorial(r)
            return result

        return choose(m-1+n-1, m-1)
