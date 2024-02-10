# https://github.com/baseballcoder1/LeetCode
#
# LeetCode 172: Factorial Trailing Zeroes
#
# Dificulty: Medium

class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_2 = 0
        num_5 = 0
        i = 1
        while True:
            if i > n:
                break

            def numfact(x, d):
                y = x
                result = 0
                while y % d == 0:
                    y //= d
                    result += 1
                return result

            num_2 += numfact(i, 2)
            num_5 += numfact(i, 5)

            i += 1
        num_10 = min(num_2, num_5)
        return num_10
