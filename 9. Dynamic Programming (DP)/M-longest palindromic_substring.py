"""
Leetcode 5: Longest Palindromic Substring

Problem Description:
Given a string `s`, return the longest palindromic substring in `s`. A palindrome is a string that reads the same forward and backward. The solution should run in **O(n^2)** time complexity, where `n` is the length of the string.

Approach:
1. **Expand Around Centers**: Iterate through each character in the string and treat each character (and the gap between characters) as a potential center of a palindrome.
2. **Expand Both Ways**: From each center, expand outward while the substring remains a palindrome.
3. **Track Longest Palindrome**: Keep track of the longest palindrome found during the process.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Base case: if string is empty or has one character, it's itself a palindrome
        if len(s) < 2:
            return s

        start, end = 0, 0  # Variables to track the start and end indices of the longest palindrome

        # Function to expand around a given center
        def expandAroundCenter(left, right):
            # Expand as long as the characters match and stay within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1   # Move left pointer outward
                right += 1  # Move right pointer outward
            # Return the length of the palindrome found
            return right - left - 1

        # Iterate through each character in the string
        for i in range(len(s)):
            # Check both odd-length and even-length palindromes
            len1 = expandAroundCenter(i, i)      # Odd-length palindrome
            len2 = expandAroundCenter(i, i + 1)  # Even-length palindrome
            maxLen = max(len1, len2)

            # Update start and end indices if a longer palindrome is found
            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2

        # Return the longest palindrome substring found
        return s[start:end + 1]

