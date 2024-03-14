'''
https://github.com/baseballcoder1/LeetCode

LeetCode 930: Binary Subarrays with Sum

LeetCode Daily Question

Difficulty: Medium
'''

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        i = [i for i in range(n) if nums[i] == 1]
        result = 0
        if goal == 0:
            j = 0
            for num in nums:
                if num == 1:
                    result += j*(j+1)//2
                    j = 0
                else:
                    j += 1
            result += j*(j+1)//2
        elif len(i) < goal:
            pass
        else:
            for j in range(len(i)-goal+1):
                k, l = j, j+goal-1
                result += 1
                if k == 0:
                    left = i[k]
                else:
                    left = i[k]-i[k-1]-1
                result += left
                if l == len(i)-1:
                    right = n-1-i[l]
                else:
                    right = i[l+1]-i[l]-1
                result += right
                result += left*right
        return result
