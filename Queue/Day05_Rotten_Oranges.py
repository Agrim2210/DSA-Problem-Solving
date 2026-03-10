"""
LeetCode 994 - Rotting Oranges
Link: https://leetcode.com/problems/rotting-oranges/

Problem:
Given an m x n grid where:
0 → empty cell
1 → fresh orange
2 → rotten orange

Every minute, a rotten orange rots its 4-directionally adjacent fresh oranges.
Return the minimum number of minutes needed until no fresh orange remains.
If impossible, return -1.

Approach (Multi-source BFS):
1. Scan the grid:
   - Count total fresh oranges.
   - Push all rotten oranges into a queue.
2. Perform BFS level by level (each level = 1 minute).
3. For each rotten orange, infect its fresh neighbors.
4. Decrease fresh count when infection happens.
5. If fresh becomes zero, return minutes taken.
6. If BFS ends and fresh > 0 → return -1.

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0

        # Step 1: initialization
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2: BFS
        while q and fresh > 0:

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1
s=Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])        )