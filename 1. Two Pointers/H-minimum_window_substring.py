""""
Problem: Minimum Window Substring (Leetcode 76)

You are given two strings s and t. Return the minimum window in s which will contain all the characters in t.
If no such window exists, return an empty string.

Efficient Approach:
- We use the **sliding window technique** to find the smallest substring.
- Maintain two pointers (left and right) to represent the window, and a counter to track how many characters from t are in the current window.
- The right pointer expands the window, and once all characters are found, the left pointer shrinks it to find the smallest window.
- This approach ensures an optimal time complexity of **O(N)**, where N is the length of s.
"""

from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    # Frequency counter for characters in t
    t_count = Counter(t)
    required = len(t_count)
    
    left, right = 0, 0
    window_count = Counter()
    formed = 0

    # Store result (window length, left, right)
    result = (float('inf'), None, None)

    while right < len(s):
        char = s[right]
        window_count[char] += 1

        # If the current character count matches the target count, increment formed
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1

        # Try to contract the window from the left
        while left <= right and formed == required:
            window_length = right - left + 1
            if window_length < result[0]:
                result = (window_length, left, right)

            # Remove the character from the left of the window
            left_char = s[left]
            window_count[left_char] -= 1
            if left_char in t_count and window_count[left_char] < t_count[left_char]:
                formed -= 1
            left += 1

        # Expand the window by moving the right pointer
        right += 1

    return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]

# Example usage
print(minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
