"""
Leetcode 133: Clone Graph

Problem Description:
Given a reference to a node in a **connected undirected graph**, return a **deep copy** of the graph. Each node in the graph contains a value and a list of its neighbors. The graph is represented as an adjacency list, where each node's neighbors are represented by a list of nodes. You must implement an algorithm to clone the graph using **O(n)** time complexity, where `n` is the number of nodes.

Approach:
1. **BFS or DFS Traversal**: Use either Depth-First Search (DFS) or Breadth-First Search (BFS) to traverse the graph. In this solution, we will use DFS.
2. **Hash Map for Cloning**: Maintain a hash map (`visited`) to keep track of the original nodes and their corresponding cloned nodes.
3. **Recursion**: For each node, recursively clone its neighbors and update the cloned graph.
4. **Return the Cloned Graph**: Once the entire graph is cloned, return the reference to the cloned node.
"""

from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None  # Edge case: If the node is None, return None

        visited = {}  # Dictionary to map original nodes to their clones

        def dfs(node: Node) -> Node:
            if node in visited:
                return visited[node]  # Return the already cloned node

            # Create a new clone node
            clone_node = Node(node.val)
            visited[node] = clone_node  # Map the original node to the clone

            # Recursively clone all the neighbors
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))

            return clone_node

        # Start DFS from the given node and return its clone
        return dfs(node)
