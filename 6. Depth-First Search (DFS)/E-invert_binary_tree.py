"""
Leetcode 226: Invert Binary Tree

Problem Description:
Given the root of a binary tree, invert the tree and return its root.
In other words, for each node in the tree, swap its left and right children.

Problem Type: Tree Traversal / DFS (Recursion)

Approach:
1. **Recursive DFS**: Use a recursive depth-first search (DFS) to invert the tree.
2. **Base Case**: If the current node is `None`, return `None` (nothing to invert).
3. **Swap**: For the current node, swap its left and right children.
4. **Recursive Call**: Continue recursively inverting the left and right subtrees.
5. **Return**: Return the root after the entire tree has been inverted.

Example Tree Before Inversion:
       1
      / \
     2   3
    / \
   4   5

Example Tree After Inversion:
       1
      / \
     3   2
        / \
       5   4

Time Complexity: O(n)
Space Complexity: O(h) → height of the tree (due to recursion stack)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left  # Swap left and right
    invertTree(root.left)
    invertTree(root.right)
    
    return root

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

inverted_root = invertTree(root)

# Helper function to print tree in preorder (for verification)
def preorder(node):
    if node:
        print(node.val, end=' ')
        preorder(node.left)
        preorder(node.right)

preorder(inverted_root)  # Output: 1 3 2 5 4
