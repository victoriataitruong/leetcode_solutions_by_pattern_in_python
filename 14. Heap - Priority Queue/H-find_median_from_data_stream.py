"""
Leetcode 295: Find Median from Data Stream

Problem Description:
The problem requires designing a data structure that efficiently supports the following operations:
1. addNum(int num) - Adds a number to the data structure.
2. findMedian() - Returns the median of all numbers added so far.

Efficient Approach:
We use a two-heap solution:
- A max-heap (left) to store the smaller half of the numbers.
- A min-heap (right) to store the larger half of the numbers.

The heaps are balanced such that:
- The max-heap (left) has at most one more element than the min-heap (right).
- The median is either the max of the max-heap (if odd total count) or the average of both heap tops (if even total count).

Time Complexity:
- addNum: O(log n) due to heap insertion.
- findMedian: O(1) since it only looks at the tops of the heaps.
"""

import heapq

class MedianFinder:

    def __init__(self):
        # Max heap (simulated with negative values for Python's min-heap)
        self.left = []  # max-heap (for the smaller half of numbers)
        self.right = []  # min-heap (for the larger half of numbers)

    def addNum(self, num: int) -> None:
        # Insert into the max-heap (simulated by using negative values)
        heapq.heappush(self.left, -num)

        # Balance heaps: if the largest number in the left heap is greater than the smallest in the right heap
        if self.left and self.right and -self.left[0] > self.right[0]:
            heapq.heappush(self.right, -heapq.heappop(self.left))

        # Ensure balance between heaps: left can have at most 1 more element than right
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        # If left heap has more elements, the median is the top of the left heap
        if len(self.left) > len(self.right):
            return -self.left[0]
        # If heaps are balanced, the median is the average of both tops
        return (-self.left[0] + self.right[0]) / 2.0

# Example usage
finder = MedianFinder()
finder.addNum(1)
finder.addNum(2)
print(finder.findMedian())  # Output: 1.5
finder.addNum(3)
print(finder.findMedian())  # Output: 2

