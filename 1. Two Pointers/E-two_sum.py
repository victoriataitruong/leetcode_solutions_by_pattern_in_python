"""
Leetcode 1: Two Sum

Problem Description:
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. The solution must be solved in **O(n)** time complexity, where `n` is the number of elements in the array.

Approach:
1. **Hash Map**: Use a hash map to store the indices of the elements we have already seen.
2. **Iterate Through the Array**: For each element, calculate the complement (the number needed to reach the target) and check if it exists in the hash map.
3. **Return Indices**: If the complement exists, return the current index and the index of the complement from the hash map.
"""
class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store the numbers and their indices
        num_map = {}

        # Iterate through the array of numbers
        for i, num in enumerate(nums):
            complement = target - num

            # If the complement is found in the dictionary, return the indices
            if complement in num_map:
                return [num_map[complement], i]

            # Otherwise, store the number with its index in the dictionary
            num_map[num] = i

        # Return an empty list if no solution is found
        return []

# Example usage
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]


            