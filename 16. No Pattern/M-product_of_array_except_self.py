"""
Leetcode 238: Product of Array Except Self

Problem Description:
Given an integer array `nums`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. You must solve it without using division and in **O(n)** time complexity, where `n` is the number of elements in the array.

Approach:
1. **Prefix and Suffix Products**: We will compute two arrays: one for the prefix product (product of all elements before the current index) and another for the suffix product (product of all elements after the current index).
2. **Iterate Through the Array**: Calculate the result for each index using the prefix and suffix products.
3. **Final Result**: Multiply the prefix and suffix products to get the desired product for each index.
"""

from typing import List  # Import the List type hint from the typing module

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step 1: Initialize the output array
        n = len(nums)
        output = [1] * n

        # Step 2: Calculate the prefix products and store them in the output array
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Step 3: Calculate the suffix products and update the output array
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        # Step 4: Return the result array containing the product of all elements except the current one
        return output

#EXAMPLE USAGE:
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 4]
print(solution.productExceptSelf(nums1))  # Output: [24, 12, 8, 6]

# Example 2
nums2 = [-1, 1, 0, -3, 3]
print(solution.productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]

