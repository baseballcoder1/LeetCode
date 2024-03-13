'''
https://github.com/baseballcoder1/LeetCode

LeetCode 2485: Find the Pivot Integer

LeetCode Daily Question

Difficulty: Easy
'''

class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n+1):
            sum1 = i*(1+i)/2
            sum2 = (n-i+1)*(i+n)/2
            if sum1 == sum2:
                return i
        else:
            return -1
