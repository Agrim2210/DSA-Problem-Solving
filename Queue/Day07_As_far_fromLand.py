'''
---------------------------------------------------------------
LeetCode 1162 : As Far from Land as Possible
Problem Link : https://leetcode.com/problems/as-far-from-land-as-possible/

Pattern Used : Multi Source BFS (Grid Traversal)

---------------------------------------------------------------
Approach

Instead of calculating distance from every water cell to land,
we reverse the thinking and start BFS from ALL LAND cells.



Distance Spread Example:

Land (1)        -> distance 0
Adjacent water  -> distance 1
Next layer      -> distance 2
Next layer      -> distance 3

We push all land cells into queue initially.
Then perform BFS in 4 directions.

Whenever we reach a water cell:
    grid[new] = grid[current] + 1

This updates its distance from nearest land.

The last expanded cell will be the farthest water cell.

Edge Cases
1. If there is no land -> return -1
2. If grid has only land -> return -1

Time Complexity  : O(n^2)
Space Complexity : O(n^2)
---------------------------------------------------------------
'''
from collections import deque

class Solution(object):
    def maxDistance(self, grid):

        n = len(grid)
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

    
        if not q or len(q) == n*n:
            return -1

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:

            r, c = q.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:

                    
                    grid[nr][nc] = grid[r][c] + 1

                    
                    q.append((nr, nc))

        return grid[r][c] - 1
s=Solution()
print(s.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))