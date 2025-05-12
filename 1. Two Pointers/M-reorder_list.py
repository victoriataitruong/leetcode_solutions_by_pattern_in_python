"""
Leetcode 143: Reorder List

Problem Description:
Given a singly linked list, reorder it such that the nodes are rearranged in the following order: 
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → L3 → Ln-3 → .... You must solve it in O(n) time complexity and O(1) space complexity.

Approach:
1. **Find the Middle of the List**: Use the slow and fast pointer technique to find the middle node of the linked list.
2. **Reverse the Second Half**: Reverse the second half of the linked list starting from the middle.
3. **Merge the Two Halves**: Merge the first half and the reversed second half by alternating the nodes.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        second_half = slow.next
        slow.next = None  # Break the list into two halves
        prev = None
        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node
        
        # Step 3: Merge the two halves
        first_half = head
        second_half = prev
        while second_half:
            # Save the next nodes
            tmp1 = first_half.next
            tmp2 = second_half.next

            # Reorder the nodes
            first_half.next = second_half
            second_half.next = tmp1

            # Move the pointers forward
            first_half = tmp1
            second_half = tmp2

#EXAMPLE USAGE:
# Helper function to print the linked list
def print_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Example 1: List: 1 -> 2 -> 3 -> 4 -> 5
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

solution = Solution()
solution.reorderList(head1)

# Output the result after reordering
print_list(head1)
# Expected Output: 1 -> 5 -> 2 -> 4 -> 3

