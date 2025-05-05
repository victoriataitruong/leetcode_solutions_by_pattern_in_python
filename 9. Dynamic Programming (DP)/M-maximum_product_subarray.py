"""
Leetcode 152: Maximum Product Subarray

Problem Description:
Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) that has the largest product. The solution must be solved in **O(n)** time complexity, where `n` is the number of elements in the array.

Approach:
1. **Two Tracking Variables**: Maintain two variables, `max_prod` and `min_prod`, to track the maximum and minimum product up to the current index. This helps in cases where negative numbers are involved, which can flip the sign of the product.
2. **Iterate Through the Array**: For each element, compute the possible new products by including the current element. The new maximum product will either be the element itself, the element multiplied by the previous maximum product, or the element multiplied by the previous minimum product (in case of negative numbers).
3. **Update Maximum Product**: Continuously update the global maximum product as you iterate through the array.
"""

class Solution:
    def maxProduct(self, nums):
        # Edge case: if the array is empty, return 0
        if not nums:
            return 0

        # Initialize max and min products to the first element of the array
        max_prod = min_prod = result = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # If the number is negative, swap max_prod and min_prod
            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            # Update max_prod and min_prod
            max_prod = max(num, max_prod * num)  # Max product can either be the number itself or previous max_prod multiplied by the number
            min_prod = min(num, min_prod * num)  # Min product can either be the number itself or previous min_prod multiplied by the number

            # Update the result with the maximum product encountered so far
            result = max(result, max_prod)

        return result
    
#EXAMPLE USAGE:
solution = Solution()
print(solution.maxProduct([2, 3, -2, 4]))  # Output: 6
print(solution.maxProduct([-2, 0, -1]))    # Output: 0
