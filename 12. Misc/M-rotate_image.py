"""
Leetcode 48: Rotate Image

Problem Description:
Given an `n x n` 2D matrix representing an image, rotate the image 90 degrees clockwise. You must solve this problem in-place, meaning you cannot use extra space except for the given matrix. The matrix is square (n x n), and the rotation should be done in-place by modifying the matrix directly.

Approach:
1. **Transpose the Matrix**: First, swap the rows with columns of the matrix.
2. **Reverse Each Row**: After transposing, reverse each row to complete the 90-degree rotation.
3. **In-place Modifications**: The solution must be done without using extra space, so we modify the matrix directly during the transposition and reversal steps.
"""

class Solution:
    def rotate(self, matrix):
        n = len(matrix)  # Get the size of the matrix (n x n)

        # Step 1: Transpose the matrix by swapping elements at (i, j) with (j, i)
        for i in range(n):
            for j in range(i + 1, n):  # Only swap above the diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row to complete the 90-degree rotation
        for i in range(n):
            matrix[i].reverse()  # Reverse each row in place


# Example usage
solution = Solution()

# Example matrix (3x3)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rotate the matrix
solution.rotate(matrix)

# Print the rotated matrix
for row in matrix:
    print(row)

# Expected Output:
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]
