"""
Leetcode 417: Pacific Atlantic Water Flow

Problem Description:
Given a matrix of integers representing heights above sea level, you are to find all the coordinates (i, j) where water can flow to both the Pacific and Atlantic oceans. Water can flow from a cell to another cell if the height of the second cell is greater than or equal to the first cell. The Pacific ocean is on the left and top edges of the matrix, while the Atlantic ocean is on the right and bottom edges of the matrix. You must return all coordinates where water can reach both oceans.

Approach:
1. **DFS (Depth-First Search)**: Use DFS to explore the matrix starting from the edges where water can flow to the oceans. For both oceans, we perform DFS from their respective borders.
2. **Mark Reachable Cells**: During DFS, we mark cells that can reach the Pacific and Atlantic oceans. This is done by maintaining two boolean matrices to track which cells can reach which ocean.
3. **Intersection of Reachable Cells**: Once we have marked cells that can reach both oceans, the intersection of the two matrices gives us the solution.
"""

class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        
        pacific_reach = [[False] * cols for _ in range(rows)]
        atlantic_reach = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c, ocean_reach, prev_height):
            # Check boundaries and conditions for DFS
            if r < 0 or r >= rows or c < 0 or c >= cols or ocean_reach[r][c] or matrix[r][c] < prev_height:
                return
            
            # Mark current cell as reachable for the ocean
            ocean_reach[r][c] = True
            
            # Explore the 4 directions (down, up, right, left)
            dfs(r + 1, c, ocean_reach, matrix[r][c])  # Down
            dfs(r - 1, c, ocean_reach, matrix[r][c])  # Up
            dfs(r, c + 1, ocean_reach, matrix[r][c])  # Right
            dfs(r, c - 1, ocean_reach, matrix[r][c])  # Left
        
        # Perform DFS from the Pacific ocean's borders (top and left)
        for r in range(rows):
            dfs(r, 0, pacific_reach, matrix[r][0])  # Left border
            dfs(r, cols - 1, atlantic_reach, matrix[r][cols - 1])  # Right border

        # Perform DFS from the Atlantic ocean's borders (bottom and right)
        for c in range(cols):
            dfs(0, c, pacific_reach, matrix[0][c])  # Top border
            dfs(rows - 1, c, atlantic_reach, matrix[rows - 1][c])  # Bottom border

        # Find intersection of the cells that can reach both oceans
        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific_reach[r][c] and atlantic_reach[r][c]:
                    result.append([r, c])

        return result

solution = Solution()
matrix1 = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 2],
    [5, 1, 1, 2, 4]
]
print(solution.pacificAtlantic(matrix1))  
# Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

matrix2 = [
    [2, 1],
    [1, 2]
]
print(solution.pacificAtlantic(matrix2))  
# Output: [[0, 0], [0, 1], [1, 0], [1, 1]]
