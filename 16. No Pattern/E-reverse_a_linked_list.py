"""
Leetcode 206: Reverse Linked List

Problem Description:
Given the head of a singly linked list, reverse the list and return its reversed head.

Approach:
1. **Pointers**: Initialize two pointers: `prev` (to keep track of the previous node) and `current` (to traverse the list).
2. **Traverse and Reverse**: Iterate through the linked list. For each node, store the next node, reverse the current node's `next` pointer to point to `prev`, and then move both `prev` and `current` one step forward.
3. **Return Reversed List**: After the iteration, `prev` will be pointing to the new head of the reversed linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            # Temporarily store the next node
            nextNode = current.next
            # Reverse the link: point current node's next to prev
            current.next = prev
            # Move prev and current one step forward
            prev = current
            current = nextNode

        # Return prev as the new head after the reversal is complete
        return prev

# Example usage:
# Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Calling the reverseList function
solution = Solution()
reversed_head = solution.reverseList(head)

# Output the reversed list
# Expected output: 5 -> 4 -> 3 -> 2 -> 1
current = reversed_head
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next
