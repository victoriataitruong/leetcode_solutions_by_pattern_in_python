"""
Leetcode 54: Spiral Matrix

Problem Description:
Given an `m x n` matrix, return all elements of the matrix in spiral order. Starting from the top-left corner, traverse the matrix in a spiral pattern (right, down, left, up) and continue until all elements have been visited. The solution should be efficient, working within **O(m * n)** time complexity, where `m` and `n` are the number of rows and columns in the matrix, respectively.

Approach:
1. **Define Boundaries**: Keep track of the boundaries of the matrix (top, bottom, left, right).
2. **Spiral Traversal**: Use a while loop to iterate until all elements are visited. In each iteration, traverse the matrix in one direction (right, down, left, or up), and adjust the boundaries accordingly.
3. **Return Result**: After traversing the entire matrix, return the collected elements in spiral order.
"""
class Solution:
    def spiralOrder(self, matrix):
        result = []
        
        if not matrix:
            return result
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # Traverse from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # Traverse from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result
#EXAMPLE USAGE

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

solution = Solution()
print(solution.spiralOrder(matrix))
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

