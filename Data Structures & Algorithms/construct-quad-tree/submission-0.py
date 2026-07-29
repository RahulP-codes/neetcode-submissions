"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def quad(si, sj, n):
            print(f"starting {si}, {sj}, {n}")
            if n == 1:
                print(f"returning because n = 1")
                return Node(grid[si][sj], 1)

            num = grid[si][sj]
            isLeaf = True
            for i in range(si, si+n):
                if not isLeaf:
                    break
                for j in range(sj, sj+n):
                    if grid[i][j] != num:
                        isLeaf = False
                        break

            print(f"isLeaf: {isLeaf}")

            if isLeaf:
                print(f"returning all same {num}")
                return Node(num, isLeaf)
            else:
                a = int(n/2)
                topLeft = quad(si, sj, a)
                topRight = quad(si, sj+a, a)
                bottomLeft = quad(si+a, sj, a)
                bottomRight = quad(si+a, sj+a, a)

            print("returning a Node with subNodes")
            return Node(0, isLeaf, topLeft, topRight, bottomLeft, bottomRight)

        return quad(0, 0, len(grid))
