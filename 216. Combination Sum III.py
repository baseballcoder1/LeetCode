'''
https://github.com/baseballcoder1/LeetCode

LeetCode 216: Combination Sum III

Difficulty: Medium
'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def combine(a, k, n):
            if k == 1:
                if n in a:
                    yield [n]
                    return
            for i in range(len(a)):
                x = a[i]
                if x <= n-1:
                    for l in combine(a[i+1:], k-1, n-x):
                        yield [x] + l

        if k == 0:
            return []
        a = list(range(1,10))
        return list(combine(a, k, n))
