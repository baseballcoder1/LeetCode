'''
https://github.com/baseballcoder1/LeetCode

LeetCode 173: Binary Search Tree Iterator

Difficulty: Medium
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inorder(node):
        for i in 0, 1, 2:
            if i == 0 or i == 2:
                if i == 0:
                    child = node.left
                else:
                    child = node.right
                if child is None:
                    continue
                for childnode in BSTIterator.inorder(child):
                    yield childnode
            else:
                yield node

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = (x for x in BSTIterator.inorder(root))
        self.val = None
        self.valid = False

    def next(self) -> int:
        if not self.valid:
            self.val = next(self.nodes).val
            self.valid = True
        self.valid = False
        return self.val

    def hasNext(self) -> bool:
        if not self.valid:
            try:
                self.val = next(self.nodes).val
                self.valid = True
                return True
            except StopIteration:
                return False
        else:
            return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()