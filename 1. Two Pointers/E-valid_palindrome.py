"""
Leetcode 125: Valid Palindrome

Problem Description:
Given a string `s`, return `True` if it is a palindrome, or `False` otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Approach:
1. **Two Pointer Technique**: Use two pointers, one at the start and one at the end of the string.
2. **Character Comparison**: Skip non-alphanumeric characters and compare the characters at the two pointers.
3. **Check Equality**: If the characters at the pointers do not match, return `False`.
4. **Update Pointers**: Move the pointers inward and continue the process until they meet or cross.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: one at the beginning and one at the end of the string
        left, right = 0, len(s) - 1

        # Iterate until the two pointers meet
        while left < right:
            # Skip non-alphanumeric characters by moving the left pointer forward
            if not s[left].isalnum():
                left += 1
                continue
            # Skip non-alphanumeric characters by moving the right pointer backward
            if not s[right].isalnum():
                right -= 1
                continue

            # Compare characters at both pointers (case insensitive)
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward to continue checking
            left += 1
            right -= 1

        # If no mismatches were found, return True indicating the string is a palindrome
        return True

# Example usage
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal, Panama"))  # Output: True
print(solution.isPalindrome("race a car"))  # Output: False

