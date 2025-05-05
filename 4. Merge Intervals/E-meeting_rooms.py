"""
Leetcode 252: Meeting Rooms

Problem Description:
You are given an array of intervals where each interval is represented as a pair [start, end]. The task is to determine if a person can attend all meetings. A person can attend all meetings if and only if no two meetings overlap in time.

Approach:
1. **Sort the Intervals**: Sort the intervals based on their start times.
2. **Check for Overlaps**: After sorting, compare each meeting with the next one. If the end time of the current meeting is greater than the start time of the next meeting, return false.
3. **Return Result**: If no overlaps are found, return true.

Time Complexity: **O(n log n)** (due to sorting)
Space Complexity: **O(1)** (in-place sorting)
"""

def canAttendMeetings(intervals):
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Check for overlaps by comparing consecutive intervals
    for i in range(1, len(intervals)):
        if intervals[i - 1][1] > intervals[i][0]:
            return False

    return True

# Example usage:
print(canAttendMeetings([[0, 30], [35, 50], [60, 90]]))  # Output: True
print(canAttendMeetings([[0, 30], [25, 50], [60, 90]]))  # Output: False
