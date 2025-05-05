"""
Leetcode 21: Merge Two Sorted Lists

Problem Description:
Given the heads of two sorted linked lists `l1` and `l2`, merge them into a single sorted list and return its head. The merge should be done in a way that maintains the order of elements.

Approach:
1. **Dummy Node**: Create a dummy node that serves as the starting point of the merged list. This simplifies edge cases like empty lists.
2. **Two Pointers**: Use two pointers to traverse both `l1` and `l2`. Compare the current nodes and attach the smaller node to the merged list.
3. **Exhaust Remaining Nodes**: After traversing one list, append the remaining elements of the other list.
4. **Return the Merged List**: Return the node after the dummy node, which is the head of the merged list.

Time complexity: O(n + m), where `n` and `m` are the lengths of `l1` and `l2` respectively.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        # Create a dummy node to simplify the merge process
        dummy = ListNode(0)
        current = dummy

        # Traverse both lists until one of them is fully traversed
        while l1 and l2:
            # Compare the current nodes of both lists and add the smaller one to the merged list
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            # Move the current pointer to the newly added node
            current = current.next

        # If one list is exhausted, append the other list to the merged list
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        # Return the merged list, starting from the node after the dummy node
        return dummy.next

# Example usage:
# Create some sample lists
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

solution = Solution()
merged_list = solution.mergeTwoLists(l1, l2)

# Print the merged list
current = merged_list
while current:
    print(current.val, end=" -> ")
    current = current.next
