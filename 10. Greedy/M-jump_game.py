"""
Leetcode 55: Jump Game

Problem Description:
Given an array of non-negative integers `nums`, where each element represents your maximum jump length from that position, return `true` if you can reach the last index, or `false` otherwise. The goal is to determine if we can jump from the start (index 0) to the end of the array. We can jump from any index `i` to index `i + nums[i]`.

Approach:
1. **Greedy Algorithm**: Maintain a variable `farthest` to keep track of the furthest index that can be reached. 
2. **Iterate through the Array**: For each index `i`, check if it's reachable (i.e., `i <= farthest`). If reachable, update `farthest` to the maximum of its current value or `i + nums[i]`.
3. **Check if End is Reachable**: If at any point, `farthest` reaches or exceeds the last index, return `true`. If after processing all indices, `farthest` is still less than the last index, return `false`.
"""

class Solution:
    def canJump(self, nums):
        # Initialize the variable to track the farthest index we can reach
        farthest = 0

        # Loop through the array
        for i in range(len(nums)):
            # If the current index is beyond the farthest we can reach, return False
            if i > farthest:
                return False

            # Update the farthest index we can reach
            farthest = max(farthest, i + nums[i])

            # If we've already reached or passed the last index, return True
            if farthest >= len(nums) - 1:
                return True

        # If we finish the loop and haven't returned, we cannot reach the last index
        return False

