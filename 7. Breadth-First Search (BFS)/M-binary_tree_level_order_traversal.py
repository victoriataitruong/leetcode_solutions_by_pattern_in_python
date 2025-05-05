""""
Leetcode 102: Binary Tree Level Order Traversal

Problem Description:
Given the root of a binary tree, return the level order traversal of its nodes' values 
(i.e., from left to right, level by level).

Approach:
1. **BFS (Breadth-First Search)**: Use a queue to traverse the tree level by level.
2. **Queue Structure**: Each entry in the queue will hold a node and its level information.
3. **Tracking Levels**: Maintain a list of lists to store node values at each level.
4. **Result Building**: As you visit each node, append its value to the appropriate level list.

Complexity Analysis:
- **Time Complexity**: O(n) — Each node is visited once.
- **Space Complexity**: O(n) — In the worst case, the queue could hold all nodes at the deepest level.
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        # If the tree is empty, return an empty list
        if not root:
            return []

        # Initialize the queue with the root node and its level
        queue = deque([(root, 0)])
        result = []

        # BFS traversal
        while queue:
            # Dequeue the front element
            node, level = queue.popleft()

            # If this is the first node in a new level, add a new array
            if len(result) == level:
                result.append([])

            # Append the current node's value to the correct level
            result[level].append(node.val)

            # Add the left and right children to the queue with their corresponding level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        # Return the collected level order traversal
        return result

# Example usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]

