"""
Problem: Leetcode 53 - Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

The optimal approach is Kadane’s Algorithm, which uses a greedy strategy and dynamic programming.
The idea is to iterate through the array, keeping track of the current subarray sum. If the sum becomes
negative, we reset it to 0 since a negative sum would not contribute to a maximum sum subarray.
This solution runs in O(n) time complexity.
"""

class Solution:
    def maxSubArray(self, nums):
        max_sum = float('-inf')  # Stores the maximum subarray sum found
        current_sum = 0  # Stores the current subarray sum

        for num in nums:  # Iterate through each element in the array
            current_sum += num  # Add the current number to the running sum
            max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is greater

            # If current sum becomes negative, reset it to 0 (start new subarray)
            if current_sum < 0:
                current_sum = 0

        return max_sum  # Return the maximum subarray sum found

#EXAMPLE USAGE: 
solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print(solution.maxSubArray([1]))  # Output: 1


