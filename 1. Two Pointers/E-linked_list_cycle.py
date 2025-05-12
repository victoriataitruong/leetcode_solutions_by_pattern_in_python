"""
Leetcode 141: Linked List Cycle

Problem Description:
Given a linked list, determine if it has a cycle in it. A cycle means that the linked list's last node points to one of the previous nodes, creating a loop.
Return True if there is a cycle, otherwise return False.

Problem Type:
Two Pointers (Fast & Slow) → Floyd's Cycle Detection Algorithm (Tortoise and Hare)

Approach:
1. **Floyd’s Cycle-Finding Algorithm**: Use two pointers (slow and fast).
2. **Move slow by 1 step, fast by 2 steps**: If the list has a cycle, the fast pointer will eventually meet the slow pointer inside the cycle.
3. **Return True if they meet**: Otherwise, if fast reaches the end (null), return False (no cycle).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

# Example usage:
# Creating nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Connecting nodes to form a cycle: 3 → 2 → 0 → -4 → (back to node2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Cycle formed here

print(hasCycle(node1))  # Output: True
