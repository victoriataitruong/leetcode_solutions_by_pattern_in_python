"""
Leetcode 191: Number of 1 Bits

Problem Description:
You are given an unsigned integer and need to return the number of '1' bits it has (also known as the Hamming weight).

Approach:
1. **Efficient Approach using Bitwise AND Operation**: 
   - Use the operation `n &= (n - 1)` to flip the least significant '1' bit to '0'. 
   - Each time a '1' bit is flipped, increment the count.
   - Repeat until `n` becomes 0.

Time Complexity: O(k), where k is the number of '1' bits in `n`.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0  # Initialize count of 1 bits
        while n != 0:  # Loop until n becomes 0
            n &= (n - 1)  # Flip the least significant '1' bit to '0'
            count += 1  # Increase count for each '1' bit removed
        return count  # Return total count of 1 bits


# Example usage
solution = Solution()
print(solution.hammingWeight(11))  # Output: 3 (binary 1011)
