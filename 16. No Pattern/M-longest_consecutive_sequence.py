"""
Problem: Longest Consecutive Sequence (Leetcode 128)

Given an unsorted array of integers nums, return the length of the longest 
consecutive elements sequence.

Example:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].

Constraints:
- Time complexity must be O(n).
"""

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0  # If nums is empty, return 0
        
        num_set = set(nums)  # Convert the list to a set for O(1) lookups
        longest_streak = 0  # Initialize the longest streak counter

        for num in num_set:
            # Only start counting from the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num  # Start of a new sequence
                current_streak = 1  # Initialize streak length

                # Expand the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the maximum streak found so far
                longest_streak = max(longest_streak, current_streak)

        return longest_streak  # Return the longest consecutive sequence length

#EXAMPLE USAGE:
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4



