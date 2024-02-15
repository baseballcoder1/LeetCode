'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1926: Nearest Exit from Entrance in Maze

Difficulty: Medium
'''

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        class Node:
            def __init__(self, i, j):
                self.row = i
                self.col = j
                self.children = []

        def neighbors(width, height, x, y):
            result = []
            for i in x-1, x+1:
                j = y
                if 0 <= i <= width-1:
                    result.append([i, j])
            i = x
            for j in y-1, y+1:
                if 0 <= j <= height-1:
                    result.append([i, j])
            return result

        m = len(maze)
        n = len(maze[0])
        nodes = [[None]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if maze[i][j] == ".":
                    nodes[i][j] = Node(i, j)
        for i in range(m):
            for j in range(n):
                if nodes[i][j] is not None:
                    for l, k in neighbors(n, m, j, i):
                        if nodes[k][l] is not None:
                            nodes[i][j].children += [nodes[k][l]]
        
        current = [nodes[entrance[0]][entrance[1]]]
        visited = list(current)
        steps = 0
        while True:
            for node in current:
                if node == nodes[entrance[0]][entrance[1]]:
                    continue
                if node.row == 0 or node.row == m-1:
                    return steps
                if node.col == 0 or node.col == n-1:
                    return steps
            new = []
            for node in current:
                for j, i in neighbors(n, m, node.col, node.row):
                    if nodes[i][j] is None:
                        continue
                    if nodes[i][j] in visited:
                        continue
                    new += [nodes[i][j]]
                    visited += [nodes[i][j]]
            if len(new) == 0:
                return -1
            current = new
            steps += 1
        return steps
