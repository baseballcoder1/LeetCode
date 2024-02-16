'''
https://github.com/baseballcoder1/LeetCode

LeetCode 2336: Smallest Number in Infinite Set

Difficulty: Medium
'''

class SmallestInfiniteSet:

    def __init__(self):
        self.start = 1
        self.extra = {}

    def popSmallest(self) -> int:
        if len(self.extra) != 0:
            minextra = min(self.extra.keys())
            result = minextra
            del self.extra[minextra]
        else:
            result = self.start
            self.start += 1
        return result

    def addBack(self, num: int) -> None:
        if num == self.start-1:
            self.start -= 1
        elif num >= self.start:
            pass
        else:
            if num not in self.extra:
                self.extra[num] = 1
        x = self.start
        while x in self.extra:
            del self.extra[x]
            self.start = x
            x -= 1

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
