# Python Data Types and Data Structures Examples

# ----------------------
# Primitive Data Types
# ----------------------

# Integer
age = 30  # Whole number
type_of_age = type(age)

# Float
height = 5.9  # Decimal number
type_of_height = type(height)

# String
name = "Alice"  # Sequence of characters
type_of_name = type(name)

# Boolean
is_student = True  # Logical value: True or False
type_of_is_student = type(is_student)

# NoneType
nothing = None  # Represents absence of a value
type_of_nothing = type(nothing)

# ----------------------
# Basic Data Structures
# ----------------------

# List
my_array = [1, 2, 3, 4, 5]
print(my_array)

# Tuple
coordinates = (10.0, 20.0)

# Set
unique_numbers = {1, 2, 3, 1}
unique_numbers.add(4)

# Dictionary
person = {"name": "Alice", "age": 30, "height": 5.9}

# ----------------------
# Custom ArrayList Class
# ----------------------

class ArrayList:
    def __init__(self):
        self.array = []

    def append(self, value):
        self.array.append(value)

    def remove(self, value):
        if value in self.array:
            self.array.remove(value)
        else:
            print(f"{value} not found in the list.")

    def get(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            print("Index out of range.")
            return None

    def size(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)

arraylist = ArrayList()
arraylist.append(10)
arraylist.append(20)
arraylist.append(30)
print(arraylist)
print(arraylist.get(1))
arraylist.remove(20)
print(arraylist)
print(arraylist.size())

# ----------------------
# AVL Tree
# ----------------------

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        if not root:
            return
        print(root.key)
        self.pre_order(root.left)
        self.pre_order(root.right)

tree = AVLTree()
root = None
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = tree.insert(root, key)
print("Preorder traversal of the AVL tree:")
tree.pre_order(root)

# ----------------------
# Binary Search Tree
# ----------------------

class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if not node.left:
                node.left = BSTNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.value:
            if not node.right:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or node.value == key:
            return node
        if key < node.value:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        res = []
        if node:
            res += self._inorder(node.left)
            res.append(node.value)
            res += self._inorder(node.right)
        return res

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.value:
            node.left = self._delete(node.left, key)
        elif key > node.value:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:", bst.inorder())
result = bst.search(40)
print("Search for 40:", "Found" if result else "Not found")
bst.delete(20)
print("Inorder traversal after deleting 20:", bst.inorder())

# ----------------------
# Graph
# ----------------------

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def print_graph(self):
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.print_graph()

# ----------------------
# Hash Table
# ----------------------

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return sum(ord(char) for char in str(key)) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = []
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if bucket:
            for k, v in bucket:
                if k == key:
                    return v
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if bucket:
            for i, (k, _) in enumerate(bucket):
                if k == key:
                    bucket.pop(i)
                    return

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")

ht = HashTable()
ht.insert("name", "Alice")
ht.insert("age", 30)
ht.insert("city", "New York")
print(ht.get("name"))
print(ht.get("age"))
print(ht.get("city"))
ht.remove("age")
print(ht.get("age"))
