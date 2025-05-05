"""
Problem: Serialize and Deserialize Binary Tree (Leetcode 297)

You are tasked with implementing an algorithm to **serialize** and **deserialize** a binary tree.
Serialization involves converting a binary tree into a string, while deserialization converts that string back into the original tree.
You should use an efficient approach to perform both operations.

Efficient Approach:
- We use **pre-order traversal** to serialize the binary tree into a string.
- In serialization, each node is recorded by its value, and null nodes are represented by the string "None".
- The deserialization function will reconstruct the tree by parsing the string and recursively rebuilding nodes in the pre-order sequence.
- This approach ensures an optimal time complexity of **O(N)**, where N is the number of nodes in the tree, as we visit each node once.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Constructor for creating a new TreeNode.
        :param val: Value of the node (default is 0).
        :param left: Left child node (default is None).
        :param right: Right child node (default is None).
        """
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """
        Serializes a binary tree to a string.
        :param root: Root of the binary tree.
        :return: Serialized string.
        """
        def preorder(node):
            if not node:
                return ['None']  # Represent null nodes as 'None'
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        
        return ','.join(preorder(root))

    def deserialize(self, data):
        """
        Deserializes a string to reconstruct the binary tree.
        :param data: Serialized string.
        :return: Root of the reconstructed binary tree.
        """
        data_list = data.split(',')
        
        def build_tree():
            if not data_list:
                return None  # Base case for empty list
            value = data_list.pop(0)  # Get the first element
            if value == 'None':
                return None  # Null node case
            node = TreeNode(int(value))  # Create new TreeNode
            node.left = build_tree()  # Recursively build left subtree
            node.right = build_tree()  # Recursively build right subtree
            return node
        
        return build_tree()

# Example usage:
codec = Codec()
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized = codec.serialize(root)
print(f"Serialized: {serialized}")  # Serialized tree
deserialized = codec.deserialize(serialized)
print(f"Deserialized root value: {deserialized.val}")  # Root value of deserialized tree

