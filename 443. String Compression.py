'''
https://github.com/baseballcoder1/LeetCode

LeetCode 443: String Compression

Difficulty: Medium
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        group = chars[0]
        i = 1
        j = 0
        for ch in chars[1:]:
            if ch == group:
                i += 1
            else:
                chars[j] = group
                j += 1
                if i > 1:
                    a = list(str(i))
                    chars[j:j+len(a)] = a
                    j += len(a)
                group = ch
                i = 1
        chars[j] = group
        j += 1
        if i > 1:
            a = list(str(i))
            chars[j:j+len(a)] = a
            j += len(a)
        return j
