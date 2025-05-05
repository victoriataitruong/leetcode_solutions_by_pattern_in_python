"""
Leetcode 100: Same Tree

Problem Description:
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Approach:
1. **Base Case 1**: If both trees are `None`, they are considered the same.
2. **Base Case 2**: If one tree is `None` and the other is not, they are not the same.
3. **Node Value Check**: If the values of the nodes are different, return `False`.
4. **Recursive Check**: Recursively check the left and right subtrees of both trees.
5. **Return the Result**: If both subtrees are the same, return `True`.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Base case: if both trees are null, they are the same
        if not p and not q:
            return True

        # Base case: if one tree is null and the other is not, they are not the same
        if not p or not q:
            return False

        # If the values at the current nodes are different, return false
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees of both trees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage (with TreeNode definition)
# Example trees:
# Tree 1:   1
#          /   \
#         2     3
#
# Tree 2:   1
#          /   \
#         2     3
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

solution = Solution()
print(solution.isSameTree(p, q))  # Output: True
