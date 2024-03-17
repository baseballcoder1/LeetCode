'''
https://github.com/baseballcoder1/LeetCode

LeetCode 57: Insert Interval

LeetCode Daily Question

Difficulty: Medium
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a = sorted(intervals + [newInterval], key=lambda x: x[0])
        result = []
        b = []
        for interval in a:
            def merge(x, y):
                if x == []:
                    return [], y
                if x[0] <= y[0] <= y[1] <= x[1]:
                    return [], x
                if x[1] >= y[0]:
                    return [], [x[0], y[1]]
                return x, y
            x, y = merge(b, interval)
            if x != []:
                result += [x]
            b = y
        if b != []:
            result += [b]
        return result
