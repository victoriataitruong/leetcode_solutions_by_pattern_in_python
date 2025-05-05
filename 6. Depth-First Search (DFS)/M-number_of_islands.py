"""
Leetcode 200: Number of Islands

Problem Description:
Given a 2D grid of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You need to implement an algorithm that returns the number of islands in the given grid. The algorithm must have a time complexity of O(m * n), where `m` is the number of rows and `n` is the number of columns in the grid.

Approach:
1. **Flood Fill/DFS**: For each unvisited land ('1'), we perform a Depth-First Search (DFS) to mark all the connected land as visited.
2. **Mark Visited Land**: During the DFS, we convert all connected land ('1') to water ('0') to avoid revisiting the same land.
3. **Count Islands**: Each time we find an unvisited land, we increment the island count and initiate a DFS to mark the entire island.
"""

class Solution:
    def numIslands(self, grid):
        # Edge case: if grid is empty, return 0
        if not grid or not grid[0]:
            return 0

        island_count = 0
        rows = len(grid)
        cols = len(grid[0])

        # Helper function for DFS to mark connected land
        def dfs(r, c):
            # Check if the current cell is out of bounds or water ('0')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            # Mark the current land as visited by turning it into water ('0')
            grid[r][c] = '0'

            # Explore the four adjacent directions (up, down, left, right)
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Iterate through the entire grid
        for i in range(rows):
            for j in range(cols):
                # When we encounter unvisited land ('1')
                if grid[i][j] == '1':
                    # Increment the island count
                    island_count += 1
                    # Perform DFS to mark all land connected to this island
                    dfs(i, j)

        # Return the total count of islands
        return island_count

#EXAMPLE USAGE:
solution = Solution()
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(solution.numIslands(grid1))  # Output: 1

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(solution.numIslands(grid2))  # Output: 3

