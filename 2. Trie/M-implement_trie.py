"""
Leetcode 208: Implement Trie (Prefix Tree)

Problem Description:
A **Trie** (pronounced as "try") or **prefix tree** is a tree data structure used for efficient retrieval of keys in a dataset of strings. Implement the Trie class:

- **`insert(word)`**: Inserts the string `word` into the trie.
- **`search(word)`**: Returns `true` if the string `word` is in the trie (exact match).
- **`startsWith(prefix)`**: Returns `true` if there is any string in the trie that starts with the given `prefix`.

Approach:
1. **TrieNode Class**: Create a `TrieNode` class with:
   - A dictionary `children` to store child nodes.
   - A boolean `is_end` to mark the end of a word.
2. **Trie Class**: Implement the methods:
   - `insert()`: Traverse the trie nodes, adding nodes as needed.
   - `search()`: Traverse the trie and return `True` only if `is_end` is `True` for the last character.
   - `startsWith()`: Traverse the trie and return `True` if the prefix exists.
"""
class TrieNode:
    def __init__(self):
        # Dictionary to hold children nodes (each representing a character)
        self.children = {}
        # Boolean to mark the end of a word
        self.is_end = False

class Trie:
    def __init__(self):
        # Root node is initialized as an empty TrieNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # If character is not present, add a new TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the next node
            node = node.children[char]
        # Mark the end of the word
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # If character is not found, the word is not in the Trie
            if char not in node.children:
                return False
            # Move to the next node
            node = node.children[char]
        # Return true only if the word's end is properly marked
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            # If character is not found, prefix does not exist
            if char not in node.children:
                return False
            # Move to the next node
            node = node.children[char]
        # Prefix exists in the Trie
        return True


