""""
Leetcode 98: Validate Binary Search Tree

Problem Description:
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
1. The left subtree of a node contains only nodes with keys **less than** the node's key.
2. The right subtree of a node contains only nodes with keys **greater than** the node's key.
3. Both the left and right subtrees must also be binary search trees.

Approach:
1. **Recursive In-Order Traversal**: Perform an in-order traversal while keeping track of the previously visited node.
2. **Validation Check**: If the current node's value is not greater than the previous node's value, the tree is not a valid BST.
3. **Bounds-Based Recursion**: Alternatively, track valid ranges (min and max) for each node to ensure BST conditions hold.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            
            return True
        
        return helper(root)

#Example Usage:
# Example tree:
#     2
#    / \
#   1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

solution = Solution()
print(solution.isValidBST(root))  # Output: True

