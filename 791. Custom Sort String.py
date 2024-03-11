'''
https://github.com/baseballcoder1/LeetCode

LeetCode 791: Custom Sort String

LeetCode Daily Question

Difficulty: Medium
'''

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        a = list(filter(lambda x: x in order, s))
        b = list(filter(lambda x: x not in order, s))
        return "".join(sorted(a, key=lambda x: order.index(x)) + b)
