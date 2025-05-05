"""
Leetcode 91: Decode Ways

Problem Description:
Given a string `s` consisting of digits, return the total number of ways to decode it. A mapping of 'A' = 1, 'B' = 2, ..., 'Z' = 26 is used to decode the string. For example, "12" can be decoded as "AB" (1 2) or "L" (12). The decoding may involve multiple digits and must be done in such a way that the digits form valid letters (1-26). The input string may have leading zeros and is guaranteed to be a non-empty string.

Approach:
1. **Dynamic Programming (DP)**: Use dynamic programming to keep track of the number of ways to decode the string at each position.
2. **State Representation**: Let `dp[i]` represent the number of ways to decode the substring `s[0:i]`.
3. **Base Case**: The empty string has one way to decode, so `dp[0] = 1`.
4. **Transition**: 
   - If `s[i-1]` is a valid digit (1-9), then `dp[i] += dp[i-1]`.
   - If `s[i-2:i]` is a valid two-digit number (10-26), then `dp[i] += dp[i-2]`.
5. **Return**: The result will be `dp[len(s)]`, which will give the total number of ways to decode the entire string.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: if the string is empty or starts with '0', there's no valid decoding
        if not s or s[0] == '0':
            return 0

        # Initialize dp array: dp[i] stores number of ways to decode s[:i]
        dp = [0] * (len(s) + 1)

        # Base cases
        dp[0] = 1  # Empty string has 1 way to decode
        dp[1] = 1 if s[0] != '0' else 0

        # Iterate over the string starting from index 2
        for i in range(2, len(s) + 1):
            # Check if single digit is valid (1-9)
            if '1' <= s[i - 1] <= '9':
                dp[i] += dp[i - 1]

            # Check if two-digit number is valid (10-26)
            if '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        return dp[len(s)]

# Example usage
solution = Solution()
print(solution.numDecodings("226"))  # Output: 3


