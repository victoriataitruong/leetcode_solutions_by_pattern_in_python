"""
Leetcode 190: Reverse Bits

Problem Description:
Given a 32-bit unsigned integer, reverse its bits and return the result.

Approach:
- We iterate through all 32 bits of the number.
- Shift the result left by 1 to make space for the new bit.
- Extract the least significant bit (LSB) from `n` and add it to `result`.
- Right shift `n` by 1 to process the next bit.
- Repeat this process for all 32 bits.

This ensures that the bits are reversed efficiently in constant time.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0  # Stores the reversed bits
        for i in range(32):
            result = (result << 1) | (n & 1)  # Shift left and add the LSB of n
            n >>= 1  # Right shift to process the next bit
        return result & 0xFFFFFFFF  # Ensure the result is within a 32-bit unsigned integer

# Example usage
solution = Solution()
print(solution.reverseBits(43261596))  # Output: 964176192
