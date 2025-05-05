"""
Leetcode 15: 3Sum

Problem Description:
Given an array of integers `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:
- i != j, i != k, j != k
- nums[i] + nums[j] + nums[k] == 0
The solution must be solved in **O(n^2)** time complexity, where `n` is the number of elements in the array.

Approach:
1. **Sort the Array**: Sorting the array helps to efficiently handle duplicates and helps in applying the two-pointer technique.
2. **Iterate with a Fixed Element**: Iterate through the array, fixing one element and trying to find the other two using the two-pointer approach.
3. **Two-pointer Technique**: For each fixed element, use two pointers to find pairs that sum up to the negative of the fixed element.
4. **Avoid Duplicates**: Skip over any duplicate elements to ensure that each triplet is unique.

"""
class Solution:
    def threeSum(self, nums):
        """
        Given an array of integers `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]`
        such that: i != j, i != k, j != k and nums[i] + nums[j] + nums[k] == 0.
        The solution must be solved in O(n^2) time complexity.
        """
        
        # Sort the array to simplify finding unique triplets
        nums.sort()

        # Initialize an array to store the result triplets
        result = []

        # Iterate over the array with index `i`
        for i in range(len(nums) - 2):
            # Skip duplicates: If the current number is the same as the previous one, continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum up to the negative of the current number
            left, right = i + 1, len(nums) - 1

            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]

                # If the sum is zero, we've found a valid triplet
                if triplet_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers to the next unique values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move pointers towards the center after finding a valid triplet
                    left += 1
                    right -= 1
                elif triplet_sum < 0:
                    # If the sum is less than zero, move the left pointer to the right to increase the sum
                    left += 1
                else:
                    # If the sum is greater than zero, move the right pointer to the left to decrease the sum
                    right -= 1

        # Return the list of all unique triplets
        return result

# Example usage
solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
