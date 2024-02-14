'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1679: Max Number of K-Sum Pairs

Difficulty: Medium
'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        result = 0
        for key in list(d.keys()):
            while True:
                if key not in d:
                    break
                need = k - key
                if need in d:
                    if key == need:
                        if d[key] == 1:
                            break
                    d[key] -= 1
                    if d[key] == 0:
                        del d[key]
                    d[need] -= 1
                    if d[need] == 0:
                        del d[need]
                    result += 1
                else:
                    break
        return result
