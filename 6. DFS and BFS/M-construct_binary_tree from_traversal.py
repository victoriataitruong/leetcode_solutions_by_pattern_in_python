"""
Leetcode 105: Construct Binary Tree from Preorder and Inorder Traversal

Problem Description:
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- `preorder` and `inorder` consist of unique values.
- Each value in `inorder` appears exactly once in `preorder`.
- The assumption is that the given traversals are valid and represent the same binary tree.

Approach:
1. **Base Condition:** If there are no elements in `preorder` or `inorder`, return `None` (empty tree).
2. **Root Node Identification:** The first element in `preorder` is always the root of the current subtree.
3. **Index Mapping:** Use a dictionary to map each value in `inorder` to its index for O(1) lookup.
4. **Recursive Construction:** Recursively build the left and right subtrees by dividing the `inorder` array around the root index.
5. **Return the Root Node:** The tree will be constructed recursively following this logic.
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # Create a map to store index of each value in inorder for quick lookup
        index_map = {value: index for index, value in enumerate(inorder)}
        
        def arrayToTree(preLeft: int, preRight: int, inLeft: int, inRight: int) -> Optional[TreeNode]:
            if preLeft > preRight:
                return None
            
            # The first element in preorder is always the root
            root_value = preorder[preLeft]
            root = TreeNode(root_value)
            
            # Find the index of the root in inorder
            root_index = index_map[root_value]
            
            # Number of nodes in the left subtree
            left_tree_size = root_index - inLeft
            
            # Recursively build the left subtree
            root.left = arrayToTree(preLeft + 1, preLeft + left_tree_size, inLeft, root_index - 1)
            
            # Recursively build the right subtree
            root.right = arrayToTree(preLeft + left_tree_size + 1, preRight, root_index + 1, inRight)
            
            return root
        
        return arrayToTree(0, len(preorder) - 1, 0, len(inorder) - 1)

