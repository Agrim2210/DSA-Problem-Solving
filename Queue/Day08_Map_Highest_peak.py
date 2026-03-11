# Problem: Map of Highest Peak
# Link: https://leetcode.com/problems/map-of-highest-peak/
# Approach: Multi-Source BFS

# Idea:
# All water cells have height = 0.
# We push all water cells into queue first.
# Then perform BFS to assign heights to land cells.
# Each neighbor gets height = current height + 1.

from collections import deque

class Solution(object):
    def highestPeak(self, isWater):
        
        rows = len(isWater)
        cols = len(isWater[0])
        
        q = deque()
        
        height = [[-1 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    q.append((i, j))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                
                nr = r + dr
                nc = c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and height[nr][nc] == -1:
                    
                    height[nr][nc] = height[r][c] + 1
                    q.append((nr, nc))
        
        return height
s=Solution()
print(s.highestPeak([[0,0],[0,1]])        )