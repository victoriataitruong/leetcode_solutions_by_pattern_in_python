""""
LeetCode Problem 269: Alien Dictionary

Problem Description:
You are given a list of words from an alien dictionary, where the order of characters is different from the order in the English alphabet. You need to determine the lexicographical order of the characters in the alien language.

Example 1:
text
Copy
Edit
Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"
Example 2:
text
Copy
Edit
Input: words = ["z", "x"]
Output: "zx"
Example 3:
text
Copy
Edit
Input: words = ["abc", "ab"]
Output: ""
Explanation: The given order is invalid, because the prefix "ab" is longer than the word "abc", which is impossible in a lexicographical order.
Solution Approach:
This problem can be solved using Topological Sorting because it asks us to find an ordering of characters (nodes) in a directed graph where edges represent the constraints imposed by the words.

Steps:
Create a Graph: We will treat each character as a node and the order between characters as directed edges. For example, if wrt comes before wrf, it implies that t comes before f.

Topological Sorting: We will perform a topological sort on the directed graph. If a cycle is detected, it means the ordering is impossible, and we return an empty string.

Kahn's Algorithm (for Topological Sort): We can use Kahn's algorithm, which is an efficient way to do topological sorting using a BFS approach and a queue.

Algorithm:
Build the graph using the constraints from the words.

Use Kahn’s algorithm to perform topological sorting.

Return the result as a string if the topological sort is successful; otherwise, return an empty string.

"""
from collections import defaultdict, deque

def alienOrder(words):
    # Step 1: Build the graph and in-degree map
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    # Initialize in-degree for all characters
    for word in words:
        for char in word:
            in_degree[char] = 0  # Initialize in-degree to 0 for each character
    
    # Step 2: Build the graph
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        
        # Find the first different character to establish the order
        for j in range(min_len):
            if word1[j] != word2[j]:
                # Create a directed edge word1[j] -> word2[j]
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
    
    # Step 3: Topological sort (Kahn's algorithm)
    # Initialize the queue with nodes that have in-degree 0 (no dependencies)
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1  # Remove the edge from the graph
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Step 4: If the result length is not equal to the number of unique characters, return ""
    if len(result) != len(in_degree):
        return ""  # Cycle detected or not all nodes were visited
    
    return ''.join(result)

# Example Usage:
words1 = ["wrt", "wrf", "er", "ett", "rftt"]
words2 = ["z", "x"]
words3 = ["abc", "ab"]

print(alienOrder(words1))  # Output: "wertf"
print(alienOrder(words2))  # Output: "zx"
print(alienOrder(words3))  # Output: ""