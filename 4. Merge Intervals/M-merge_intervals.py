"""
Leetcode 56: Merge Intervals

Problem Description:
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input. The intervals are sorted by the start time.

Approach:
1. **Sort Intervals**: First, sort the intervals based on the start time. This allows us to easily check for overlapping intervals in a single pass.
2. **Iterate Through the Sorted Intervals**: Loop through each interval, and check if it overlaps with the last merged interval.
3. **Merge Intervals**: If an interval overlaps, we merge it with the last one by updating the end time of the last merged interval.
4. **No Overlap**: If there is no overlap, we add the current interval to the result list.
5. **Return the Result**: At the end, return the list of merged intervals.

"""
class Solution:
    def merge(self, intervals):
        # Step 1: Sort the intervals based on the start value of each interval
        intervals.sort(key=lambda x: x[0])

        # Initialize the result list with the first interval
        merged = []

        # Step 2: Iterate through the sorted intervals
        for interval in intervals:
            # If merged is empty or no overlap, simply add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, so merge the intervals
                merged[-1][1] = max(merged[-1][1], interval[1])

        # Return the merged intervals
        return merged
#EXAMPLE USAGE:
solution = Solution()
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]
print(solution.merge([[1, 4], [4, 5]]))  # Output: [[1, 5]]

