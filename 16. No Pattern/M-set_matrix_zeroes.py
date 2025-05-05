"""
Leetcode 73: Set Matrix Zeroes

Problem Description:
Given an `m x n` matrix, if an element in the matrix is 0, its entire row and column should be set to 0. You must solve it in **O(1)** space complexity. 

Approach:
1. **Use the first row and first column to mark the rows and columns to be zeroed**: We can use the first row and column to store the state of other rows and columns. If matrix[i][j] is 0, mark matrix[i][0] and matrix[0][j] as 0.
2. **Process the matrix from the bottom-right corner**: After marking the rows and columns, traverse the matrix starting from the bottom-right corner to avoid overwriting the first row and column prematurely.
3. **Handle the first row and first column separately**: Since we used the first row and column to store marks, we need to handle these rows and columns after processing the rest of the matrix.

"""
class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # Check if the first row has any zeros
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))

        # Check if the first column has any zeros
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row and first column to mark zeros
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the row
                    matrix[0][j] = 0  # Mark the column

        # Set matrix cells to zero based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

solution = Solution()
solution.setZeroes(matrix)

print(matrix)
# Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]



