"""
Problem Description:
Leetcode 124 - Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
A node can only appear in the path at most once. The path does not necessarily need to pass through the root.

The goal is to return the maximum sum possible for any path in the tree.

Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000.

Example:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The maximum path sum is obtained from the path 15 -> 20 -> 7.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_sum = float('-inf')  # Initialize the global maximum path sum

    def maxPathSum(self, root: TreeNode) -> int:
        """
        Helper function for DFS traversal to compute max gain from each node.
        :param node: Current node in the traversal.
        :returns: Maximum path sum starting from the given node.
        """
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0  # Base case: null node contributes zero to the path

            # Recursively compute max gains from left and right subtrees
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Compute the max path sum that includes the current node
            current_sum = node.val + left_gain + right_gain

            # Update the global maximum if this path is the new highest
            self.max_sum = max(self.max_sum, current_sum)

            # Return the maximum path sum extending from this node to one of its children
            return node.val + max(left_gain, right_gain)

        dfs(root)  # Start DFS traversal from the root
        return self.max_sum  # Return the final maximum path sum

# Example usage
root = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.maxPathSum(root))  # Output: 6

