'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1268: Search Suggestions System

Difficulty: Medium
'''

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class Trie:
            class Node:
                def __init__(self):
                    self.children = [None] * 26
                    self.complete = False

            def __init__(self):
                self.root = Trie.Node()

            def ctoidx(c):
                return ord(c)-ord("a")

            def idxtoc(i):
                return chr(ord("a")+i)

            def add(self, word):
                x = self.root
                for c in word:
                    ctoidx = Trie.ctoidx
                    if x.children[ctoidx(c)] is None:
                        x.children[ctoidx(c)] = Trie.Node()
                    x = x.children[ctoidx(c)]
                x.complete = True

            def search(self, prefix):
                result = []
                x = self.root
                for c in prefix:
                    ctoidx = Trie.ctoidx
                    if x.children[ctoidx(c)] is None:
                        return result
                    x = x.children[ctoidx(c)]
                if x.complete:
                    result.append(prefix)
                nodes = [x]
                nodech = {x: prefix}
                while True:
                    new = []
                    for node in nodes:
                        for i in range(26):
                            child = node.children[i]
                            if child is not None:
                                new.append(child)
                                nodech[child] = nodech[node] + Trie.idxtoc(i)
                                if child.complete:
                                    result.append(nodech[child])
                    if len(new) == 0:
                        break
                    nodes = new
                return result

        trie = Trie()
        for product in products:
            trie.add(product)
        result = []
        for i in range(len(searchWord)):
            result.append(sorted(trie.search(searchWord[:i+1]))[:3])
        return result
