"""
Leetcode 217: Contains Duplicate

Problem Description:
Given an integer array `nums`, return `True` if any value appears at least twice in the array, and `False` if every element is distinct.

Problem Type: Duplicate Detection using Hashing

Approach:
1. **Initialize a Set**: Create an empty set to keep track of numbers we've already seen.
2. **Iterate Through the Array**: For each number:
   - If the number is already in the set, return `True` immediately (a duplicate is found).
   - Otherwise, add the number to the set.
3. **Return False if No Duplicates Found**: If we complete the iteration without finding duplicates, return `False`.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: True

Example 2:
Input: nums = [1, 2, 3, 4]
Output: False

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True

Time Complexity: O(n)
Space Complexity: O(n)
"""

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
print(containsDuplicate([1, 2, 3, 4]))        # Output: False
print(containsDuplicate([1, 2, 3, 1]))        # Output: True
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True
