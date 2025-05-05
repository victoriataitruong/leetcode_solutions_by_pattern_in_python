"""
Problem: Merge k Sorted Lists (Leetcode 23)

You are given an array of k linked lists, where each linked list is sorted in ascending order. 
Your task is to merge all these k linked lists into one sorted linked list and return the head of the merged list.

Efficient Approach:
- We use a **min-heap (priority queue)** to keep track of the smallest element among the k lists.
- Extract the minimum element from the heap, add it to the result list, and push the next element from that list into the heap.
- This approach ensures an optimal time complexity of **O(N log k)**, where N is the total number of nodes and k is the number of lists.
"""

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def mergeKLists(lists):
        # Edge case: if the list is empty, return None
        if not lists or len(lists) == 0:
            return None
        
        # Create a min-heap
        min_heap = []
        
        # Add the first node of each list to the heap
        for i in range(len(lists)):
            if lists[i]:
                # Use a tuple (node value, list index, node) for heap comparisons
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        
        # Dummy node to build the merged list
        dummy = ListNode(0)
        curr = dummy
        
        while min_heap:
            # Pop the smallest element from the heap
            val, idx, node = heapq.heappop(min_heap)
            curr.next = node  # Attach the smallest node to the result list
            curr = curr.next  # Move the pointer forward
            
            if node.next:  # If the current node has a next node, push it to the heap
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        
        return dummy.next  # Return the merged list (excluding dummy node)

# Example usage
# Assuming lists are ListNode instances
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]

solution = Solution()
merged_head = solution.mergeKLists(lists)

# Print merged list
current = merged_head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next


