'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1750: Minimum Length of String After Deleting Similar Ends

LeetCode Daily Question

Difficulty: Medium
'''

class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        j = len(s)-1
        while True:
            if i == j:
                return 1
            ch1 = s[i]
            ch2 = s[j]
            if ch1 != ch2:
                break
            while s[i] == ch1:
                i += 1
                if i == j:
                    break
            while s[j] == ch2:
                if i == j:
                    break
                j -= 1
            if i == j:
                if s[i] == ch1:
                    return 0
                else:
                    return 1
        return j-i+1
