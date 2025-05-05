"""
Problem: LeetCode 371 - Sum of Two Integers

Given two integers `a` and `b`, return the sum of the two integers 
without using the `+` or `-` operators.

Approach:
We use bitwise operations to simulate addition:
1. XOR (`^`) is used to calculate the sum without carrying.
2. AND (`&`) followed by a left shift (`<<`) is used to determine the carry.
3. We repeat this process until there is no carry.
4. Since Python handles integers differently than languages with fixed-width integers,
   we manually constrain the values to 32-bit signed integers using masks.
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # Mask to get last 32 bits
        MAX_INT = 0x7FFFFFFF  # Max positive 32-bit integer

        while b != 0:
            carry = (a & b) << 1  # Carry
            a = (a ^ b) & MASK  # Sum without carry
            b = carry & MASK  # Apply mask to carry

        # If a is a positive number within 32 bits, return as is
        # Else return the two's complement negative number
        return a if a <= MAX_INT else ~(a ^ MASK)
    
#EXAMPLE USAGE:
solution = Solution()
print(solution.getSum(1, 2))  # Output: 3
print(solution.getSum(-2, 3)) # Output: 1



