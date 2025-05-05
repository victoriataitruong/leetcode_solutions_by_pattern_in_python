""""
Leetcode 57: Insert Interval

Problem:
Given an array of non-overlapping intervals sorted by their start time, insert a new interval into the correct position, merging any overlapping intervals if necessary.

Example:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Constraints:
- The input intervals are sorted in ascending order by start time.
- The new interval may overlap with multiple existing intervals.
- The output should also be sorted and merged if necessary.

Approach:
We iterate through the intervals while keeping track of three cases:
1. Intervals that end before the new interval starts (no merging needed).
2. Overlapping intervals (merge them into one larger interval).
3. Intervals that start after the merged interval (no merging needed, just add them to the result).
This results in an O(n) time complexity solution.
"""

class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # Step 1: Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge all intervals that overlap with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval (or the new interval if no merge happened)
        result.append(newInterval)

        # Step 3: Add all remaining intervals that start after the new interval ends
        while i < n:
            result.append(intervals[i])
            i += 1

        return result

# Example usage
solution = Solution()
print(solution.insert([[1, 3], [6, 9]], [2, 5]))  # Output: [[1, 5], [6, 9]]
print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # Output: [[1, 2], [3, 10], [12, 16]]

