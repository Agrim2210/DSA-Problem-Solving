"""
LeetCode 542 - 01 Matrix
Link: https://leetcode.com/problems/01-matrix/

Problem
-------
Given an m x n binary matrix `mat`, return a matrix where each cell containing
1 stores the distance to the nearest 0.


Approach
--------
Use Multi-Source BFS.

Instead of running BFS from every '1', we start BFS from all '0's simultaneously.
All zero cells are inserted into the queue first.

Then BFS expands outward:
    distance of neighbor = current cell distance + 1

The first time we reach a cell gives the shortest distance to a zero.

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    mat[nr][nc] = mat[r][c] + 1

                    visited.add((nr, nc))
                    q.append((nr, nc))

        return mat

s=Solution()
mat=[[0,0,0],[0,1,0],[1,1,1]] 
print(s.updateMatrix(mat))
 