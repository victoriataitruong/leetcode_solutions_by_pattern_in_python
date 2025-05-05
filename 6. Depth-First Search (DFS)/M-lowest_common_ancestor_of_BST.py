"""
Leetcode 1123: Lowest Common Ancestor of Deepest Leaves

Problem Description:
Given a binary tree, find the lowest common ancestor (LCA) of the deepest leaves. The deepest leaves are those at the greatest depth in the tree, and the LCA is the lowest node that is a common ancestor to all of the deepest leaves. The solution should return the LCA of the deepest leaves.

Approach:
1. **Depth-First Search (DFS)**: We will traverse the tree using DFS to calculate the depth of each subtree and track the deepest leaves.
2. **Recursive Traversal**: For each node, calculate the depth of its left and right subtrees. If the current node is at the deepest level, it becomes a candidate for the LCA.
3. **Track Deepest Level**: Keep track of the maximum depth and the corresponding LCA for the deepest leaves.
4. **Return the LCA**: Once the traversal is complete, return the LCA of the deepest leaves.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # Helper function for DFS traversal
        def dfs(node):
            if not node:
                return 0, None  # Return depth 0 and no LCA if node is None
            
            left_depth, left_lca = dfs(node.left)  # Traverse left subtree
            right_depth, right_lca = dfs(node.right)  # Traverse right subtree
            
            # If left and right depths are different, return the deeper one
            if left_depth > right_depth:
                return left_depth + 1, left_lca
            elif right_depth > left_depth:
                return right_depth + 1, right_lca
            else:
                # If depths are equal, the current node is the LCA of deepest leaves
                return left_depth + 1, node
        
        # The LCA is the second element in the result of the DFS traversal
        return dfs(root)[1]

