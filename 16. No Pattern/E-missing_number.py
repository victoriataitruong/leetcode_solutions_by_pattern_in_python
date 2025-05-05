"""
Leetcode 268: Missing Number

Problem Description:
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the one number that is missing from the array.

Approach:
1. **Sum Formula**: The sum of the first `n` natural numbers is given by the formula:
   \[
   \text{expected_sum} = \frac{n(n+1)}{2}
   \]
2. **Compute Actual Sum**: Calculate the sum of all elements in `nums`.
3. **Find the Missing Number**: The missing number is the difference between the expected sum and the actual sum.
4. **Efficiency**: This approach runs in **O(n)** time complexity and uses **O(1)** extra space.
"""

class Solution:
    def missingNumber(self, nums):
        # Get the length of the array, which represents n
        n = len(nums)

        # Compute the expected sum of numbers from 0 to n
        expected_sum = (n * (n + 1)) // 2

        # Compute the actual sum of elements in nums
        actual_sum = sum(nums)

        # The missing number is the difference between the expected and actual sum
        return expected_sum - actual_sum

# Example usage
solution = Solution()
print(solution.missingNumber([3, 0, 1]))  # Output: 2
