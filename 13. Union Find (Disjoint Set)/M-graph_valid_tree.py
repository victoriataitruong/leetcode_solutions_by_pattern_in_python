"""
Leetcode 261: Graph Valid Tree

Problem Description:
Given an undirected graph with `n` nodes labeled from `0` to `n-1` and a list of edges, determine if the graph is a valid tree. A valid tree is a connected acyclic graph. Specifically:
- The graph must have exactly `n-1` edges (because a tree with `n` nodes always has `n-1` edges).
- The graph must be connected (there must be a path between every pair of nodes).

Approach:
1. **Edge Count Check**: A tree with `n` nodes must have exactly `n-1` edges.
2. **Depth-First Search (DFS)**: Use DFS to traverse the graph and check if it is connected (every node is visited) and does not contain any cycles.
3. **Cycle Detection**: If during the DFS traversal, we encounter a previously visited node (that’s not the immediate parent), we have detected a cycle.

"""
class Solution:
    def validTree(self, n, edges):
        # A valid tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Skip the edge back to the parent
                if neighbor in visited:
                    return False  # Cycle detected
                if not dfs(neighbor, node):
                    return False
            return True
        
        # Start DFS from node 0
        if not dfs(0, -1):
            return False
        
        # Check if all nodes were visited (graph is connected)
        return len(visited) == n

# Example usage
solution = Solution()
print(solution.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))  # Output: True

