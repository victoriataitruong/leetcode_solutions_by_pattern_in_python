"""
Leetcode 211: Design Add and Search Words Data Structure

Problem Description:
Design a data structure that supports adding new words and finding if a string matches any previously added word. Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds a word to the data structure.
- `bool search(word)` Returns true if there is any string in the data structure that matches `word` or false otherwise. A word may contain dots `.` where dots can match any letter.

Approach:
1. **Trie Data Structure**: Use a Trie (prefix tree) for efficient storage and retrieval.
2. **Recursive DFS Search**: Implement a recursive search function that can handle `.` wildcard characters effectively.
3. **Efficiency Consideration**: Trie enables efficient word insertion, while DFS ensures flexible searching with `.` wildcard support.
"""

class WordDictionary:
    def __init__(self):
        # Initialize the root of the Trie with an empty dictionary
        self.trie = {}

    def addWord(self, word: str) -> None:
        # Start from the root node
        node = self.trie
        for char in word:
            # Add character nodes if they don't exist
            if char not in node:
                node[char] = {}
            # Move to the next node
            node = node[char]
        # Mark the end of the word with a special flag
        node['$'] = True

    def search(self, word: str) -> bool:
        # Recursive DFS function to handle `.` wildcard
        def dfs(node, i):
            # If we've processed the entire word
            if i == len(word):
                return '$' in node  # Check for end of word flag

            char = word[i]
            if char == '.':  # Wildcard logic
                # Check all possible characters in the current node
                for child in node:
                    if child != '$' and dfs(node[child], i + 1):
                        return True
            else:  # Normal character logic
                if char in node and dfs(node[char], i + 1):
                    return True

            # No match found
            return False

        # Start DFS from the root of the Trie
        return dfs(self.trie, 0)

# Example usage
word_dict = WordDictionary()
word_dict.addWord("bad")
word_dict.addWord("dad")
word_dict.addWord("mad")
print(word_dict.search("pad"))  # Output: False
print(word_dict.search("bad"))  # Output: True
print(word_dict.search(".ad"))  # Output: True
print(word_dict.search("b.."))  # Output: True


