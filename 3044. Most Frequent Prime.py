'''
https://github.com/baseballcoder1/LeetCode

LeetCode 3044: Most Frequent Prime

Difficulty: Medium
'''

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        primes = []
        for i in range(m):
            for j in range(n):
                for xdelta in -1, 0, 1:
                    for ydelta in -1, 0, 1:
                        if xdelta == 0 and ydelta == 0:
                            continue
                        pos = [i, j]
                        s = str(mat[i][j])
                        while True:
                            pos = [pos[0]+ydelta, pos[1]+xdelta]
                            if pos[0] < 0 or pos[0] >= m or pos[1] < 0 or pos[1] >= n:
                                break
                            s += str(mat[pos[0]][pos[1]])
                            x = int(s)
                            def isprime(x):
                                for i in range(2, x):
                                    if x % i == 0:
                                        return False
                                else:
                                    return True
                            if isprime(x):
                                primes.append(x)
        d = {x: primes.count(x) for x in primes if x > 10}
        if len(d) == 0:
            return -1
        maxfreq = max(d.values())
        l = sorted(list(filter(lambda x: d[x] == maxfreq, d.keys())))
        if len(l) == 0:
            return -1
        else:
            return l[-1]
