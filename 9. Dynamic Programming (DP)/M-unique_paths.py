"""
Leetcode 62: Unique Paths

Problem Description:
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there?

Approach:
1. **Dynamic Programming (DP)**: Use a 2D DP table to store the number of ways to reach each cell. The value at each cell represents the number of ways to reach that cell from the start.
2. **Grid Initialization**: The topmost row and the leftmost column can only be reached in one way (moving all the way right or all the way down), so they are initialized to 1.
3. **Filling the DP Table**: For each remaining cell, the number of ways to reach it is the sum of the ways to reach the cell directly above it and the cell directly to its left.
4. **Return the Result**: The value at the bottom-right corner of the grid is the total number of unique paths.

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Step 1: Initialize DP table with 1s
        dp = [[1] * n for _ in range(m)]

        # Step 2: Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # Step 3: Return the bottom-right value
        return dp[m - 1][n - 1]

solution = Solution()
print(solution.uniquePaths(3, 7))  # Output: 28
print(solution.uniquePaths(3, 2))  # Output: 3

