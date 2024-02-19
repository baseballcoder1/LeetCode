'''
https://github.com/baseballcoder1/LeetCode

LeetCode 41: First Missing Positive

Difficulty: Hard
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        Needs to be O(n) time, O(1) space
        '''
        el = min(filter(lambda x: x > 0, nums), default=0)
        if el > 1:
            return 1
        else:
            d = {x: 1 for x in nums if x > 0}
            x = el+1
            while True:
                if x not in d:
                    return x
                x += 1
