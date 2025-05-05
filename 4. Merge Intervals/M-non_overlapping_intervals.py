"""
Leetcode 435: Non-overlapping Intervals

Problem Description:
Given a collection of intervals, `intervals` where `intervals[i] = [start_i, end_i]`, the task is to find the maximum number of non-overlapping intervals. You need to choose the intervals such that no two intervals overlap. The intervals are initially unsorted, and the solution should be solved in **O(n log n)** time complexity, where `n` is the number of intervals.

Approach:
1. **Sorting**: Sort the intervals based on their end times. This is key to making sure that we always pick the next interval that ends the earliest, which maximizes the remaining space for future intervals.
2. **Greedy Selection**: Initialize a variable to track the end of the last added interval. For each interval, if its start time is greater than or equal to the end time of the last added interval, select it and update the end time.
3. **Count Non-overlapping Intervals**: Keep a count of how many non-overlapping intervals are selected and return this count.

"""
class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Step 1: Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])
        
        # Step 2: Initialize variables
        end = float('-inf')  # Last end time (initially set to negative infinity)
        count = 0  # Number of intervals to remove
        
        # Step 3: Iterate over the sorted intervals
        for interval in intervals:
            # If the current interval starts after or exactly when the last selected one ends
            if interval[0] >= end:
                # We can select this interval, update the end time
                end = interval[1]
            else:
                # If intervals overlap, we discard this one
                count += 1
        
        # Step 4: Return the count of intervals to remove
        return count

#EXAMPLE USAGE:
solution = Solution()
print(solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # Output: 1
print(solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))  # Output: 2
print(solution.eraseOverlapIntervals([[1, 2], [2, 3]]))  # Output: 0


