"""
Problem: Word Search II (Leetcode 212)

You are given a 2D board of characters and a list of words. You need to find all words in the board that can be constructed by sequentially adjacent cells. Each word must be constructed by navigating horizontally or vertically to adjacent cells. Diagonal connections are not allowed. The task is to find all valid words from the list that exist in the board.

Efficient Approach:
- We use a Trie (prefix tree) to store the list of words. This allows us to efficiently check whether a sequence of characters in the board forms a valid word.
- We perform a Depth-First Search (DFS) on the board starting from each cell, recursively exploring all possible paths in all four directions (up, down, left, right).
- Each time we find a valid word (a word is completed), we add it to the result set.
- This approach ensures an optimal time complexity of O(N * M * K), where N and M are the dimensions of the board, and K is the maximum length of the word in the list. The DFS ensures we explore each path, while the Trie helps limit the search space.
- Backtracking is employed to ensure we don't revisit cells in the same search path.
"""

class TrieNode:
    def __init__(self):
        """
        Initialize a TrieNode with an empty dictionary for children
        and a flag to indicate if the node marks the end of a word.
        """
        self.children = {}  # A dictionary to store child nodes
        self.isWord = False  # A flag to indicate the node represents a valid word

class Solution:
    def findWords(self, board, words):
        """
        Given a 2D board and a list of words, find all words in the board 
        that can be constructed by navigating horizontally or vertically.
        """
        
        # Step 1: Build a Trie (prefix tree) from the list of words
        trie = TrieNode()

        def addWordToTrie(word):
            node = trie
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isWord = True

        # Insert all words into the Trie
        for word in words:
            addWordToTrie(word)

        # Step 2: Define the DFS function to search for words on the board
        def dfs(board, node, i, j, path):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == "#":
                return

            char = board[i][j]
            nextNode = node.children.get(char)
            if not nextNode:
                return  # Stop if the character is not found in the Trie

            path.append(char)  # Add character to path
            board[i][j] = "#"  # Mark cell as visited

            if nextNode.isWord:
                result.add("".join(path))  # Found a valid word

            # Explore all four directions: down, up, right, left
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                dfs(board, nextNode, i + x, j + y, path)

            # Backtrack
            board[i][j] = char
            path.pop()

        # Step 3: Initialize the result set to store found words
        result = set()

        # Step 4: Iterate through each cell in the board and start DFS
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, trie, i, j, [])

        # Step 5: Return the result as a list of words
        return list(result)

# Example usage
solution = Solution()
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]
words = ["oath", "pea", "eat", "rain"]
print(solution.findWords(board, words))  # Output: ['eat', 'oath']

