'''
https://github.com/baseballcoder1/LeetCode

LeetCode 973: K Closest Points to Origin

Difficulty: Medium
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(x, x[0]**2 + x[1]**2) for x in points]
        sorteddist = sorted(dist, key=lambda x: x[1])
        return [x for x, _ in sorteddist][:k]
