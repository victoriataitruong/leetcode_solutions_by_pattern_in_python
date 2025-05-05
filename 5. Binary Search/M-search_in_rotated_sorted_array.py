"""
Leetcode 33: Search in Rotated Sorted Array

Problem Description:
Given a rotated sorted array `nums` and an integer `target`, write a function to search for the `target` in the array. If the `target` exists, return its index, otherwise return `-1`. The array is initially sorted in ascending order but then rotated at some unknown pivot, which means the array might not be sorted at the start. You must implement an algorithm with **O(log n)** time complexity, where `n` is the number of elements in the array.

Approach:
1. **Binary Search**: Since the array is rotated, we can still use binary search, but with a slight modification to account for the rotation.
2. **Check Sorted Half**: We need to determine whether the left or right half of the array is sorted. Once we know that, we can narrow down which half of the array to search.
3. **Adjust Search Range**: Depending on whether the target is in the sorted half or the unsorted half, adjust the search range accordingly.
4. **Return Index**: If the target is found, return its index; otherwise, return `-1`.
"""

class Solution:
    def search(self, nums, target):
        # Initialize the left and right pointers for binary search
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            # Find the middle index
            mid = (left + right) // 2

            # If the target is found, return the index
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # If target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If the right half is sorted
            else:
                # If target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # If target is not found, return -1
        return -1

# Example usage:
solution = Solution()

# Example rotated sorted array
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

# Search for the target
result = solution.search(nums, target)

print(result)  # Output should be 4 (the index of target 0)



