'''
https://github.com/baseballcoder1/LeetCode

LeetCode 208: Implement Trie (Prefix Tree)

Difficulty: Medium
'''

class Trie:
    class Node:
        def __init__(self):
            self.children = [None] * 26
            self.complete = False

        def chtoidx(c):
            return ord(c)-ord("a")

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str) -> None:
        x = self.root
        for c in word:
            chtoidx = Trie.Node.chtoidx
            if x.children[chtoidx(c)] is None:
                x.children[chtoidx(c)] = Trie.Node()
            x = x.children[chtoidx(c)]
        x.complete = True

    def search(self, word: str) -> bool:
        x = self.root
        for c in word:
            chtoidx = Trie.Node.chtoidx
            if x.children[chtoidx(c)] is None:
                return False
            x = x.children[chtoidx(c)]
        return x.complete

    def startsWith(self, prefix: str) -> bool:
        x = self.root
        for c in prefix:
            chtoidx = Trie.Node.chtoidx
            if x.children[chtoidx(c)] is None:
                return False
            x = x.children[chtoidx(c)]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)