"""
Leetcode 104: Maximum Depth of Binary Tree

Problem Description:
Given the root of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Problem Type:
Recursive DFS (Depth-First Search)

Approach:
1. **Depth-First Search (DFS)**: Use recursion to traverse the tree and calculate the depth at each node.
2. **Base Case**: If the current node is `None`, return 0 (no depth).
3. **Recursive Case**: Recursively compute the depth of the left and right subtrees.
4. **Return the Maximum Depth**: For each node, the depth is 1 plus the maximum depth of its left and right subtrees.

Time Complexity: O(n)
Space Complexity: O(h) → height of the tree (due to recursion stack)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:
        return 0

    left_depth = maxDepth(root.left)  # Recurse into the left subtree
    right_depth = maxDepth(root.right)  # Recurse into the right subtree
    return 1 + max(left_depth, right_depth)  # Return 1 + the greater of the two depths

# Example usage:
# Creating a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Calling the maxDepth function
depth = maxDepth(root)

# The tree is:
#         1
#        / \
#       2   3
#      / \
#     4   5

print(depth)  # Output: 3
