'''
https://github.com/baseballcoder1/LeetCode

LeetCode 17: Letter Combinations of a Phone Number

Difficulty: Medium
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def combine(s):
            letters = {}
            letters["2"] = "abc"
            letters["3"] = "def"
            letters["4"] = "ghi"
            letters["5"] = "jkl"
            letters["6"] = "mno"
            letters["7"] = "pqrs"
            letters["8"] = "tuv"
            letters["9"] = "wxyz"
            if len(s) == 1:
                yield from letters[s[0]]
            else:
                for c in letters[s[0]]:
                    for substr in combine(s[1:]):
                        yield c + substr

        if digits == "":
            return []
        return list(combine(digits))
