"""
Leetcode 424: Longest Repeating Character Replacement

Problem Description:
You are given a string `s` and an integer `k`. You can replace any character in the string with another character at most `k` times.

Return the length of the longest substring that contains the same letter you can achieve after performing these replacements.

Approach:
1. **Sliding Window Technique**: Use two pointers (`left` and `right`) to maintain a window in the string.
2. **Character Frequency Tracking**: Track the frequency of characters in the current window using a dictionary.
3. **Max Character Count**: Maintain the maximum count of any single character in the window to determine the number of replacements required.
4. **Window Shrinking Condition**: If the window size minus the maximum character count exceeds `k`, move the `left` pointer to shrink the window.
5. **Result Calculation**: Continuously update the maximum window size during the process.
"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to count character frequency in the current window
        char_count = defaultdict(int)
        left = 0
        max_count = 0  # Maximum frequency of any character in the window
        max_length = 0  # Maximum length of valid substring

        # Iterate through the string using the 'right' pointer
        for right in range(len(s)):
            # Add the current character to the frequency dictionary
            char_count[s[right]] += 1

            # Track the maximum frequency of any character in the current window
            max_count = max(max_count, char_count[s[right]])

            # Check if the window is invalid (needs more than k replacements)
            if (right - left + 1) - max_count > k:
                # Shrink the window from the left
                char_count[s[left]] -= 1
                left += 1

            # Update the maximum valid window length
            max_length = max(max_length, right - left + 1)

        return max_length

