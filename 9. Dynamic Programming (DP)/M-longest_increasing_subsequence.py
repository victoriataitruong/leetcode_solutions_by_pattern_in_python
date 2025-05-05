"""
Leetcode 300: Longest Increasing Subsequence

Problem Description:
Given an integer array `nums`, return the length of the longest strictly increasing subsequence. A subsequence is defined as a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. The solution must be solved in **O(n log n)** time complexity, where `n` is the number of elements in the array.

Approach:
1. **Dynamic Programming with Binary Search**: We use dynamic programming along with binary search to efficiently find the longest increasing subsequence.
2. **Maintain a List**: Use a list to store the smallest possible last element for increasing subsequences of each length.
3. **Binary Search**: For each element in the array, use binary search to find the position where it can replace an element in the list to form a longer increasing subsequence.
4. **Return Length**: The length of the list at the end will be the length of the longest increasing subsequence.
"""

import bisect

class Solution:
    def lengthOfLIS(self, nums):
        # Edge case: if the list is empty, return 0
        if not nums:
            return 0
        
        # Initialize an array to store the smallest tail of all increasing subsequences
        subsequence = []
        
        # Iterate over each number in the input array
        for num in nums:
            # Use binary search to find the position to replace or append the number
            pos = bisect.bisect_left(subsequence, num)
            
            # If the position is equal to the length of the subsequence array, append the number
            if pos == len(subsequence):
                subsequence.append(num)
            else:
                subsequence[pos] = num
        
        # The length of the subsequence array is the length of the longest increasing subsequence
        return len(subsequence)

