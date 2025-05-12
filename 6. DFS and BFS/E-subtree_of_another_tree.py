"""
Leetcode 572: Subtree of Another Tree

Problem Description:
Given two binary trees `root` and `subRoot`, return true if there is a subtree of `root` that is an exact match with `subRoot`. A subtree of a tree is a tree that consists of a node in the tree and all its descendants. The solution must be solved efficiently, ideally in **O(n)** time complexity, where `n` is the number of nodes in the tree.

Approach:
1. **DFS with Tree Comparison**: We perform a depth-first search (DFS) to check if the tree rooted at the current node of `root` is identical to `subRoot`.
2. **Helper Function to Check Identity**: Use a helper function to compare two trees node by node. If they are identical, return true.
3. **Traverse the Root Tree**: We traverse the tree `root` using DFS and call the helper function to check if the subtree rooted at each node matches `subRoot`.
4. **Return Result**: If a match is found at any node, return true, otherwise, return false.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # If subRoot is None, it is trivially a subtree of any tree
        if not subRoot:
            return True
        
        # If root is None, subRoot can't be a subtree
        if not root:
            return False
        
        # Check if the current root's tree matches subRoot
        if self.isIdentical(root, subRoot):
            return True
        
        # Recurse through left and right subtrees of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isIdentical(self, root1: TreeNode, root2: TreeNode) -> bool:
        # If both trees are empty, they are identical
        if not root1 and not root2:
            return True
        
        # If one of the trees is empty and the other is not, they are not identical
        if not root1 or not root2:
            return False
        
        # If the values of the current nodes are different, the trees are not identical
        if root1.val != root2.val:
            return False
        
        # Recursively check the left and right subtrees
        return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)

# Example usage
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(0)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

solution = Solution()
print(solution.isSubtree(root, subRoot))  # Output: True
