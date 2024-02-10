'''
https://github.com/baseballcoder1/LeetCode

LeetCode 992: Subarrays with K Different Integers

Difficulty: Hard
'''

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        
        result = 0
        i = 0
        j = 0
        d = {}
        if k == 1:
            minsize = True
        else:
            minsize = False
        while j < len(nums):
            def add(d, x):
                if x not in d:
                    d[x] = 1
                else:
                    d[x] += 1
            
            def remove(d, x):
                d[x] -= 1
                if d[x] == 0:
                    del d[x]
            
            def newsize(d, x):
                if x not in d:
                    return len(d)+1
                else:
                    return len(d)
            
            x = nums[j]

            if not minsize:
                add(d, x)
                if len(d) == k-1:
                    minsize = True
                j += 1
                continue
            
            if newsize(d, x) > k:
                while len(d) != k-1:
                    remove(d, nums[i])
                    i += 1
            
            add(d, x)
            if len(d) == k:
                result += 1
                l = i
                dcopy = dict(d)
                while len(dcopy) != k-1:
                    remove(dcopy, nums[l])
                    if len(dcopy) == k:
                        result += 1
                    l += 1
            
            j += 1
        return result
