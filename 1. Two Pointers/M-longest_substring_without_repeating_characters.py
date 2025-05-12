"""
Leetcode 3: Longest Substring Without Repeating Characters

Problem Description:
Given a string `s`, find the length of the **longest substring** without repeating characters. The solution must be solved in **O(n)** time complexity, where `n` is the length of the string.

Approach:
1. **Sliding Window Technique**: Use two pointers (`left` and `right`) to represent a window that moves through the string.
2. **Hash Map for Tracking Characters**: Store characters and their most recent index in a dictionary to quickly identify duplicates.
3. **Dynamic Window Adjustment**: As the `right` pointer iterates through the string, move the `left` pointer when a duplicate character is found to maintain a valid substring.
4. **Max Length Calculation**: Track the maximum length during iteration.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store characters and their latest index
        char_index = {}
        left = 0
        max_length = 0

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # If the character is already in the dictionary and its index is within the window
            if s[right] in char_index and char_index[s[right]] >= left:
                # Move the left pointer to exclude the repeating character
                left = char_index[s[right]] + 1

            # Update the latest index of the current character
            char_index[s[right]] = right

            # Calculate the maximum length of the substring
            max_length = max(max_length, right - left + 1)

        return max_length
    
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3


