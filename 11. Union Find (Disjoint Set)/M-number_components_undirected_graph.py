"""
Leetcode 323: Number of Connected Components in an Undirected Graph

Problem Description:
You are given an integer `n`, the number of nodes in an undirected graph, and a 2D array `edges`, where each edge `edges[i] = [u, v]` connects nodes `u` and `v`. Return the number of connected components in the graph. A connected component is a set of nodes in which any node is reachable from any other node in the set.

Approach:
1. **Union-Find (Disjoint Set Union)**: The Union-Find data structure helps track and merge connected components efficiently. Initially, each node is in its own component, and the algorithm merges them as it processes the edges.
2. **Union**: For each edge, union the two nodes (if they belong to different components).
3. **Find**: To check if two nodes are connected, we find the roots of both nodes and check if they belong to the same component.
4. **Count Components**: At the end, the number of connected components will be equal to the number of unique roots in the Union-Find structure.
"""

class Solution:
    def countComponents(self, n, edges):
        # Initialize the parent array where each node is its own parent initially
        parent = list(range(n))

        # Helper function to find the root of a node with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        # Helper function to union two components
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            # If they are not already in the same component, union them
            if rootX != rootY:
                parent[rootX] = rootY

        # Iterate through each edge and union the connected nodes
        for u, v in edges:
            union(u, v)

        # Count the number of unique roots (connected components)
        components = sum(1 for i in range(n) if parent[i] == i)

        return components


