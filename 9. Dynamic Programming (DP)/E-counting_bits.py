"""
Leetcode 338: Counting Bits

Problem Description:
Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n),
`ans[i]` is the number of 1's in the binary representation of `i`.

Problem Type: Dynamic Programming

Approach:
1. **Dynamic Programming**: Use dynamic programming to build the solution.
2. **Relation**: The number of 1's in `i` is given by `dp[i // 2] + (i % 2)`.
   - `i // 2` shifts the number right by 1 (removing the least significant bit).
   - `i % 2` checks whether the least significant bit is 1 (odd) or 0 (even).
3. **Build the Result**: Create an array `dp` where `dp[i]` stores the number of 1's in the binary representation of `i`.
   Populate it using the relation for all `i` from 1 to `n`.

Example:
Input: n = 2
Output: [0, 1, 1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Time Complexity: O(n)
Space Complexity: O(n)
"""

def countBits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i // 2] + (i % 2)
    return dp

# Example usage:
print(countBits(2))  # Output: [0, 1, 1]
print(countBits(5))  # Output: [0, 1, 1, 2, 1, 2]
