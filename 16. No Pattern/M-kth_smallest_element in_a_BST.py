""""
Leetcode 230: Kth Smallest Element in a BST

Problem Description:
Given the `root` of a binary search tree (BST) and an integer `k`, return the `k`th smallest value (1-indexed) of all the values of the nodes in the tree.

Approach:
1. **Inorder Traversal**: Since an inorder traversal of a BST yields nodes in sorted order, we can efficiently find the `k`th smallest element this way.
2. **Recursive DFS**: Perform a depth-first traversal (inorder) while keeping track of the number of visited nodes.
3. **Early Stopping**: As soon as the `k`th element is found, return it to avoid unnecessary recursion.

Time Complexity: **O(H + k)** where `H` is the tree height. In the average case for a balanced BST, this is **O(log n + k)**.
Space Complexity: **O(H)** for the recursion stack.
"""
class Solution:
    def __init__(self):
        self.count = 0  # Counter for visited nodes
        self.result = None  # Stores the kth smallest value

    def kthSmallest(self, root, k):
        # Helper function to perform inorder traversal
        def inorder(node):
            if not node or self.result is not None:
                return

            # Traverse the left subtree
            inorder(node.left)

            # Process the current node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            # Traverse the right subtree
            inorder(node.right)

        # Start the inorder traversal from the root
        inorder(root)
        return self.result


