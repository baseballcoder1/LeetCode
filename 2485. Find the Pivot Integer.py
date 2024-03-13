'''
https://github.com/baseballcoder1/LeetCode

LeetCode 2485: Find the Pivot Integer

LeetCode Daily Question

Difficulty: Easy
'''

class Solution:
    def pivotInteger(self, n: int) -> int:
        def sqrt(x):
            for i in range(1, x+1):
                y = i*i
                if y == x:
                    return i
                elif y > x:
                    return None

        x = sqrt(n*(n+1)//2)
        if x is not None:
            return x
        else:
            return -1
