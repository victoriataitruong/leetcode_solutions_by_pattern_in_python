"""
Leetcode 1143: Longest Common Subsequence

Problem Description:
Given two strings `text1` and `text2`, return the length of their longest common subsequence. A subsequence of a string is a sequence that can be derived from the string by deleting some or no characters without changing the relative order of the remaining characters. A common subsequence is a subsequence that appears in both strings. You need to find the longest subsequence that appears in both strings. The solution should be optimized to work in **O(m * n)** time complexity, where `m` and `n` are the lengths of the two strings.

Approach:
1. **Dynamic Programming**: Use dynamic programming to store the lengths of the longest common subsequence for each pair of prefixes of `text1` and `text2`.
2. **DP Table**: Create a 2D table where `dp[i][j]` represents the length of the longest common subsequence of `text1[0..i-1]` and `text2[0..j-1]`.
3. **Transition**: If characters `text1[i-1]` and `text2[j-1]` match, then `dp[i][j] = dp[i-1][j-1] + 1`. Otherwise, take the maximum value between `dp[i-1][j]` and `dp[i][j-1]`.
4. **Final Answer**: The value at `dp[m][n]` will give the length of the longest common subsequence of `text1` and `text2`.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Step 1: Get the lengths of the two input strings
        m, n = len(text1), len(text2)

        # Step 2: Create a 2D DP table with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Step 3: Iterate through both strings
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Step 4: If characters match, take the value from the diagonal (previous subsequences) + 1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Step 5: Otherwise, take the maximum value from the left or top cell
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 6: Return the bottom-right cell, which contains the length of the longest common subsequence
        return dp[m][n]

#EXAMPLE USAGE    
solution = Solution()
print(solution.longestCommonSubsequence("abcde", "ace"))  # Output: 3


