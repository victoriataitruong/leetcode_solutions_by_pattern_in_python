""""
Leetcode 79: Word Search

Problem Description:
Given an `m x n` grid of characters `board` and a string `word`, return `true` if the word exists in the grid and `false` otherwise.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Approach:
1. **DFS with Backtracking**: Perform Depth-First Search (DFS) starting from each cell in the grid.
2. **Boundary Conditions**: Ensure boundary checks for valid cell positions.
3. **Visited Tracking**: Use a set to track visited cells to avoid reusing the same cell.
4. **Backtrack**: After exploring a path, backtrack to allow other possibilities.

Time Complexity: **O(m * n * 4^L)** where `m` is the number of rows, `n` is the number of columns, and `L` is the length of the word.
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index):
            if index == len(word):
                return True  # All characters matched
            
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False  # Out of bounds or character mismatch
            
            temp = board[r][c]
            board[r][c] = '#'  # Mark as visited
            
            # Explore all four directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            board[r][c] = temp  # Backtrack
            
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):  # Start DFS if first letter matches
                    return True
        
        return False
    
#EXAMPLE USAGE:
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word = "ABCCED"

solution = Solution()
print(solution.exist(board, word))  # Output: True


